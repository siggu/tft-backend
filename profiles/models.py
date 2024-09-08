# models.py

from django.db import models


class SummonerPuuid(models.Model):
    puuid = models.CharField(
        max_length=200,
        unique=True,
    )
    gameName = models.CharField(max_length=200, default="hide on bush")
    tagLine = models.CharField(max_length=20, default="KR1")
    accountId = models.CharField(max_length=200, null=True)
    profileIconId = models.IntegerField(null=True)
    summonerId = models.CharField(max_length=200, null=True)
    summonerLevel = models.IntegerField(null=True)


class SummonerMatchesByPuuid(models.Model):
    summoner_puuid = models.ForeignKey(
        SummonerPuuid,
        on_delete=models.CASCADE,
        to_field="puuid",
        related_name="matches",
    )
    match_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.summoner_puuid} - {self.match_id}"
    
class SummonerBadMatchesByPuuid(models.Model):
    summoner_puuid = models.ForeignKey(
        SummonerPuuid,
        on_delete=models.CASCADE,
        to_field="puuid",
        related_name="bad_matches",
    )
    match_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.summoner_puuid} - {self.match_id}"


# metadata
class Metadata(models.Model):
    data_version = models.PositiveIntegerField(default=0)
    match_id = models.OneToOneField(
        SummonerMatchesByPuuid,
        on_delete=models.CASCADE,
        related_name="metadata",
    )
    participants = models.TextField(max_length=650)


# info - augment
class Augment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# info - companion
class Companion(models.Model):
    content_ID = models.CharField(max_length=50)
    item_ID = models.PositiveIntegerField()
    skin_ID = models.PositiveIntegerField()
    species = models.CharField(max_length=20)


# info - mission
class Missions(models.Model):
    participant = models.ForeignKey(
        "Participants",
        on_delete=models.CASCADE,
        related_name="missions",
    )
    Assists = models.PositiveIntegerField()
    DamageDealt = models.PositiveIntegerField()
    DamageDealtToObjectives = models.PositiveIntegerField()
    DamageDealtToTurrets = models.PositiveIntegerField()
    DamageTaken = models.PositiveIntegerField()
    Deaths = models.PositiveIntegerField()
    DoubleKills = models.PositiveIntegerField()
    GoldEarned = models.PositiveIntegerField()
    GoldSpent = models.PositiveIntegerField()
    InhibitorsDestroyed = models.PositiveIntegerField()
    KillingSprees = models.PositiveIntegerField()
    Kills = models.PositiveIntegerField()
    LargestKillingSpree = models.PositiveIntegerField()
    LargestMultiKill = models.PositiveIntegerField()
    MagicDamageDealt = models.PositiveIntegerField()
    MagicDamageDealtToChampions = models.PositiveIntegerField()
    MagicDamageTaken = models.PositiveIntegerField()
    NeutralMinionsKilledTeamJungle = models.PositiveIntegerField()
    PentaKills = models.PositiveIntegerField()
    PhysicalDamageDealt = models.PositiveIntegerField()
    PhysicalDamageDealtToChampions = models.PositiveIntegerField()
    PhysicalDamageTaken = models.PositiveIntegerField()
    PlayerScore0 = models.PositiveIntegerField()
    PlayerScore1 = models.PositiveIntegerField()
    PlayerScore10 = models.PositiveIntegerField()
    PlayerScore11 = models.PositiveIntegerField()
    PlayerScore2 = models.PositiveIntegerField()
    PlayerScore3 = models.PositiveIntegerField()
    PlayerScore4 = models.PositiveIntegerField()
    PlayerScore5 = models.PositiveIntegerField()
    PlayerScore6 = models.PositiveIntegerField()
    PlayerScore9 = models.PositiveIntegerField()
    QuadraKills = models.PositiveIntegerField()
    Spell1Casts = models.PositiveIntegerField()
    Spell2Casts = models.PositiveIntegerField()
    Spell3Casts = models.PositiveIntegerField()
    Spell4Casts = models.PositiveIntegerField()
    SummonerSpell1Casts = models.PositiveIntegerField()
    TimeCCOthers = models.PositiveIntegerField()
    TotalDamageDealtToChampions = models.PositiveIntegerField()
    TotalMinionsKilled = models.PositiveIntegerField()
    TripleKills = models.PositiveIntegerField()
    TrueDamageDealt = models.PositiveIntegerField()
    TrueDamageDealtToChampions = models.PositiveIntegerField()
    TrueDamageTaken = models.PositiveIntegerField()
    UnrealKills = models.PositiveIntegerField()
    VisionScore = models.PositiveIntegerField()
    WardsKilled = models.PositiveIntegerField()


# info - trait
class Traits(models.Model):
    name = models.CharField(max_length=100)
    num_units = models.IntegerField()
    style = models.IntegerField()
    tier_current = models.IntegerField()
    tier_total = models.IntegerField()

    def __str__(self):
        return self.name


# info - unit
class Unit(models.Model):
    character_id = models.CharField(max_length=50)
    itemNames = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=5,
        blank=True,
        null=True,
    )
    rarity = models.IntegerField()
    tier = models.IntegerField()

    def __str__(self):
        return self.character_id


# info - participant
class Participants(models.Model):
    augments = models.ManyToManyField(
        Augment,
        related_name="participants",
    )
    companion = models.OneToOneField(
        Companion,
        related_name="participants",
        on_delete=models.CASCADE,
    )
    gold_left = models.PositiveIntegerField()
    last_round = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    placement = models.PositiveIntegerField(default=0)
    players_eliminated = models.PositiveIntegerField(default=0)
    puuid = models.ForeignKey(
        SummonerPuuid,
        on_delete=models.CASCADE,
        related_name="participants",
    )
    time_eliminated = models.PositiveIntegerField(default=0)
    total_damage_to_players = models.PositiveIntegerField(default=0)
    traits = models.ManyToManyField(
        Traits,
        related_name="participants",
    )
    units = models.ManyToManyField(
        Unit,
        related_name="participants",
    )


# info
class Info(models.Model):
    endOfGameResult = models.CharField(max_length=20)
    gameCreation = models.PositiveIntegerField(default=0)
    gameId = models.PositiveIntegerField(default=0)
    game_datetime = models.PositiveIntegerField(default=0)
    game_length = models.PositiveIntegerField(default=0)
    game_version = models.CharField(max_length=100)
    mapId = models.PositiveIntegerField(default=0)
    participants = models.ForeignKey(
        Participants,
        related_name="info",
        on_delete=models.CASCADE,
    )
    queueId = models.PositiveIntegerField(default=0)
    queue_id = models.PositiveIntegerField(default=0)
    tft_game_type = models.CharField(max_length=20)
    tft_set_core_name = models.CharField(max_length=20)
    tft_set_number = models.PositiveIntegerField(default=0)


# metadata + info
class SummonerMatchByMatchId(models.Model):
    match_id = models.CharField(max_length=100, primary_key=True)

    metadata = models.ForeignKey(
        Metadata,
        related_name="matchinfo",
        on_delete=models.CASCADE,
    )
    info = models.ForeignKey(
        Info,
        related_name="matchinfo",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.match_id)


# 매치 데이터 JSON으로 때려박기
class MatchDetailsByMatchId(models.Model):
    match_id = models.CharField(
        max_length=100,
        primary_key=True,
    )
    match_detail = models.JSONField(
        "json",
        default=dict,
    )


# summonerId로
# https://kr.api.riotgames.com/tft/league/v1/entries/by-summoner/?api_key=
class LeagueEntryDTO(models.Model):
    summonerId = models.CharField(max_length=200, primary_key=True)

    # summonerId가 인자로 들어가서 puuid도 foreignKey로 엮어야 하는가의 의문점
    puuid = models.CharField(max_length=200, null=True)

    leagueId = models.CharField(max_length=200, null=True)
    queueType = models.CharField(max_length=100)
    tier = models.CharField(max_length=30, null=True)
    rank = models.CharField(max_length=30, null=True)
    leaguePoints = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    veteran = models.BooleanField(default=False)
    inactive = models.BooleanField(default=False)
    freshBlood = models.BooleanField(default=False)
    hotStreak = models.BooleanField(default=False)
