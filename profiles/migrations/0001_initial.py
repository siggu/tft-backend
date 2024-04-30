# Generated by Django 5.0.2 on 2024-04-30 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Augment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Companion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_ID', models.CharField(max_length=50)),
                ('item_ID', models.PositiveIntegerField()),
                ('skin_ID', models.PositiveIntegerField()),
                ('species', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MatchDetailsByMatchId',
            fields=[
                ('match_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('match_detail', models.JSONField(default=dict, verbose_name='json')),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_version', models.PositiveIntegerField(default=0)),
                ('participants', models.TextField(max_length=650)),
            ],
        ),
        migrations.CreateModel(
            name='SummonerMatchesByPuuid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SummonerPuuid',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('accountId', models.CharField(max_length=100)),
                ('puuid', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(default='소환사닉네임', max_length=30)),
                ('profileIconId', models.PositiveIntegerField(default=0)),
                ('revisionDate', models.PositiveIntegerField(default=0)),
                ('summonerLevel', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Traits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('num_units', models.IntegerField()),
                ('style', models.IntegerField()),
                ('tier_current', models.IntegerField()),
                ('tier_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.CharField(max_length=50)),
                ('itemNames', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=5, null=True)),
                ('rarity', models.IntegerField()),
                ('tier', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gold_left', models.PositiveIntegerField()),
                ('last_round', models.PositiveIntegerField(default=0)),
                ('level', models.PositiveIntegerField(default=0)),
                ('placement', models.PositiveIntegerField(default=0)),
                ('players_eliminated', models.PositiveIntegerField(default=0)),
                ('time_eliminated', models.PositiveIntegerField(default=0)),
                ('total_damage_to_players', models.PositiveIntegerField(default=0)),
                ('augments', models.ManyToManyField(related_name='participants', to='profiles.augment')),
                ('companion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='profiles.companion')),
                ('puuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='profiles.summonerpuuid')),
                ('traits', models.ManyToManyField(related_name='participants', to='profiles.traits')),
                ('units', models.ManyToManyField(related_name='participants', to='profiles.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Missions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assists', models.PositiveIntegerField()),
                ('DamageDealt', models.PositiveIntegerField()),
                ('DamageDealtToObjectives', models.PositiveIntegerField()),
                ('DamageDealtToTurrets', models.PositiveIntegerField()),
                ('DamageTaken', models.PositiveIntegerField()),
                ('Deaths', models.PositiveIntegerField()),
                ('DoubleKills', models.PositiveIntegerField()),
                ('GoldEarned', models.PositiveIntegerField()),
                ('GoldSpent', models.PositiveIntegerField()),
                ('InhibitorsDestroyed', models.PositiveIntegerField()),
                ('KillingSprees', models.PositiveIntegerField()),
                ('Kills', models.PositiveIntegerField()),
                ('LargestKillingSpree', models.PositiveIntegerField()),
                ('LargestMultiKill', models.PositiveIntegerField()),
                ('MagicDamageDealt', models.PositiveIntegerField()),
                ('MagicDamageDealtToChampions', models.PositiveIntegerField()),
                ('MagicDamageTaken', models.PositiveIntegerField()),
                ('NeutralMinionsKilledTeamJungle', models.PositiveIntegerField()),
                ('PentaKills', models.PositiveIntegerField()),
                ('PhysicalDamageDealt', models.PositiveIntegerField()),
                ('PhysicalDamageDealtToChampions', models.PositiveIntegerField()),
                ('PhysicalDamageTaken', models.PositiveIntegerField()),
                ('PlayerScore0', models.PositiveIntegerField()),
                ('PlayerScore1', models.PositiveIntegerField()),
                ('PlayerScore10', models.PositiveIntegerField()),
                ('PlayerScore11', models.PositiveIntegerField()),
                ('PlayerScore2', models.PositiveIntegerField()),
                ('PlayerScore3', models.PositiveIntegerField()),
                ('PlayerScore4', models.PositiveIntegerField()),
                ('PlayerScore5', models.PositiveIntegerField()),
                ('PlayerScore6', models.PositiveIntegerField()),
                ('PlayerScore9', models.PositiveIntegerField()),
                ('QuadraKills', models.PositiveIntegerField()),
                ('Spell1Casts', models.PositiveIntegerField()),
                ('Spell2Casts', models.PositiveIntegerField()),
                ('Spell3Casts', models.PositiveIntegerField()),
                ('Spell4Casts', models.PositiveIntegerField()),
                ('SummonerSpell1Casts', models.PositiveIntegerField()),
                ('TimeCCOthers', models.PositiveIntegerField()),
                ('TotalDamageDealtToChampions', models.PositiveIntegerField()),
                ('TotalMinionsKilled', models.PositiveIntegerField()),
                ('TripleKills', models.PositiveIntegerField()),
                ('TrueDamageDealt', models.PositiveIntegerField()),
                ('TrueDamageDealtToChampions', models.PositiveIntegerField()),
                ('TrueDamageTaken', models.PositiveIntegerField()),
                ('UnrealKills', models.PositiveIntegerField()),
                ('VisionScore', models.PositiveIntegerField()),
                ('WardsKilled', models.PositiveIntegerField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='missions', to='profiles.participants')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endOfGameResult', models.CharField(max_length=20)),
                ('gameCreation', models.PositiveIntegerField(default=0)),
                ('gameId', models.PositiveIntegerField(default=0)),
                ('game_datetime', models.PositiveIntegerField(default=0)),
                ('game_length', models.PositiveIntegerField(default=0)),
                ('game_version', models.CharField(max_length=100)),
                ('mapId', models.PositiveIntegerField(default=0)),
                ('queueId', models.PositiveIntegerField(default=0)),
                ('queue_id', models.PositiveIntegerField(default=0)),
                ('tft_game_type', models.CharField(max_length=20)),
                ('tft_set_core_name', models.CharField(max_length=20)),
                ('tft_set_number', models.PositiveIntegerField(default=0)),
                ('participants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='profiles.participants')),
            ],
        ),
        migrations.CreateModel(
            name='SummonerMatchByMatchId',
            fields=[
                ('match_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchinfo', to='profiles.info')),
                ('metadata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchinfo', to='profiles.metadata')),
            ],
        ),
        migrations.AddField(
            model_name='metadata',
            name='match_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='metadata', to='profiles.summonermatchesbypuuid'),
        ),
        migrations.AddField(
            model_name='summonermatchesbypuuid',
            name='summoner_puuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='profiles.summonerpuuid', to_field='puuid'),
        ),
    ]
