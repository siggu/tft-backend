# meta_deck_generator.py
import os
import requests
import json
import pandas as pd
from tqdm import tqdm
from collections import defaultdict
from sklearn.cluster import KMeans
from sklearn.preprocessing import MultiLabelBinarizer

ROIT_API_KEY = os.getenv("RIOT_API_KEY")
GAME_VERSION = "14.13"
SEARCH_SCALE = 40
MIN_ITEM_USAGE = 20

# API URL 정의
CHALLENGER_API = f"https://kr.api.riotgames.com/tft/league/v1/challenger?queue=RANKED_TFT&api_key={ROIT_API_KEY}"
SUMMONER_DTO_API = lambda summonerId: f"https://kr.api.riotgames.com/tft/summoner/v1/summoners/{summonerId}?api_key={ROIT_API_KEY}"
MATCHES_BY_PUUID_API = lambda puuid, start=0, count=20: f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start={start}&count={count}&api_key={ROIT_API_KEY}"
MATCH_DATA_API = lambda match_id: f"https://asia.api.riotgames.com/tft/match/v1/matches/{match_id}?api_key={ROIT_API_KEY}"

# 챌린저 데이터 수집
def getChallengerRawData():
    response = requests.get(CHALLENGER_API).json()
    return response['entries']

# 특정 소환사 정보 수집
def getSummonerRawData(summonerId):
    response = requests.get(SUMMONER_DTO_API(summonerId)).json()
    return response

# PUUID로 매치 ID 수집
def getMatchesByPuuidData(puuid):
    response = requests.get(MATCHES_BY_PUUID_API(puuid)).json()
    return response

# 매치 ID로 매치 상세 데이터 수집
def getMatchDetailData(match_id):
    response = requests.get(MATCH_DATA_API(match_id)).json()
    return response

# 데이터 처리 및 메타 덱 도출 함수
def process_data_and_generate_meta_decks():
    challenger_entries = getChallengerRawData()
    challenger_df = pd.DataFrame(challenger_entries)
    challenger_df = challenger_df.sort_values(by='leaguePoints', ascending=False)

    # 챌린저 상위 플레이어 정보 수집
    top_players = challenger_df.head(SEARCH_SCALE)

    # 상위 플레이어들의 매치 ID 수집
    all_match_ids = set()
    for summonerId in tqdm(top_players['summonerId'], desc="Fetching Summoner Data"):
        summoner_data = getSummonerRawData(summonerId)
        puuid = summoner_data['puuid']
        matches = getMatchesByPuuidData(puuid)
        all_match_ids.update(matches)

    # 중복 제거된 매치 ID 리스트
    unique_match_ids = list(all_match_ids)

    # 매치 데이터 수집
    all_matches = []
    for match_id in tqdm(unique_match_ids, desc="Fetching Match Data"):
        match_detail = getMatchDetailData(match_id)
        all_matches.append(match_detail)

    # 필요한 데이터만 추출 및 조건에 따른 필터링
    participants_data = []
    for match in all_matches:
        if 'info' in match and 'participants' in match['info']:
            game_version = match['info']['game_version']
            queue_id = match['info']['queue_id']
            if GAME_VERSION in game_version and queue_id == 1100:
                for participant in match['info']['participants']:
                    participants_data.append(participant)

    participants_df = pd.DataFrame(participants_data)
    participants_df = participants_df[['puuid', 'placement', 'traits', 'units']]
    participants_df = participants_df.dropna()

    # 순방 컬럼 추가 (4등 이상은 순방으로 간주)
    participants_df['top4'] = participants_df['placement'].apply(lambda x: 1 if x <= 4 else 0)

    # 유닛 정보를 문자열로 변환하여 조합으로 취급
    participants_df['unit_combination'] = participants_df['units'].apply(lambda units: ','.join(sorted([unit['character_id'] for unit in units])))

    # 각 챔피언별 아이템 정보를 추출하는 함수
    def extract_champion_items(units):
        champion_items = []
        for unit in units:
            champion = unit['character_id']
            items = unit.get('itemNames', [])
            if items:
                champion_items.append((champion, items))
        return champion_items

    # 챔피언별 아이템 정보를 추출하여 새로운 데이터프레임 구성
    champion_items_data = []
    for _, row in participants_df.iterrows():
        champion_items = extract_champion_items(row['units'])
        for champion, items in champion_items:
            champion_items_data.append({
                'puuid': row['puuid'],
                'placement': row['placement'],
                'top4': row['top4'],
                'champion': champion,
                'items': items
            })

    champion_items_df = pd.DataFrame(champion_items_data)

    # 순방(4위 이상) 데이터를 기반으로 챔피언별 아이템 조합 분석
    top4_champion_items_df = champion_items_df[champion_items_df['top4'] == 1]

    # 챔피언별 아이템 사용 횟수 계산
    champion_item_usage = defaultdict(lambda: defaultdict(int))
    for _, row in top4_champion_items_df.iterrows():
        champion = row['champion']
        for item in row['items']:
            champion_item_usage[champion][item] += 1

    # 챔피언별 추천 아이템 조합 도출 (최소 40번 이상 사용된 아이템만 포함)
    recommended_items = {}
    for champion, items_dict in champion_item_usage.items():
        # items_dict를 사용된 아이템 횟수 기준으로 정렬
        sorted_items = sorted(items_dict.items(), key=lambda item: item[1], reverse=True)
        filtered_items = [item for item, count in sorted_items if count >= MIN_ITEM_USAGE]
        if len(filtered_items) >= 3:
            recommended_items[champion] = filtered_items[:3]
        else:
            recommended_items[champion] = []

    # 각 챔피언을 원핫 인코딩으로 변환
    participants_df['unit_list'] = participants_df['unit_combination'].apply(lambda x: x.split(','))
    mlb = MultiLabelBinarizer()
    unit_matrix = mlb.fit_transform(participants_df['unit_list'])

    # 원핫 인코딩된 결과를 데이터프레임으로 변환
    units_df = pd.DataFrame(unit_matrix, columns=mlb.classes_)
    participants_df = pd.concat([participants_df, units_df], axis=1)

    # K-Means 군집화
    kmeans = KMeans(n_clusters=7, random_state=42)
    participants_df['cluster'] = kmeans.fit_predict(unit_matrix)

    # 각 클러스터의 중심점 (메타 덱)
    centroids = kmeans.cluster_centers_

    # 클러스터별 챔피언 조합 빈도
    clustered_units_df = pd.DataFrame(centroids, columns=mlb.classes_)

    # 각 클러스터의 중심점에서 빈도 높은 챔피언을 메타 덱으로 도출
    meta_decks = {}
    for i, row in clustered_units_df.iterrows():
        top_champions = row.sort_values(ascending=False).head(9).index.tolist()
        meta_deck = []
        for champion in top_champions:
            items = recommended_items.get(champion, [])
            meta_deck.append((champion, items))
        meta_decks[f'Meta Deck {i+1}'] = meta_deck

    return meta_decks, champion_item_usage
