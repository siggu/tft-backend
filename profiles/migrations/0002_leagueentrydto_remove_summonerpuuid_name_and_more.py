# Generated by Django 4.0.10 on 2024-08-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueEntryDTO',
            fields=[
                ('summonerId', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('puuid', models.CharField(max_length=200, null=True)),
                ('leagueId', models.CharField(max_length=200, null=True)),
                ('queueType', models.CharField(max_length=100)),
                ('tier', models.CharField(max_length=30, null=True)),
                ('rank', models.CharField(max_length=30, null=True)),
                ('leaguePoints', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('veteran', models.BooleanField(default=False)),
                ('inactive', models.BooleanField(default=False)),
                ('freshBlood', models.BooleanField(default=False)),
                ('hotStreak', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='summonerpuuid',
            name='name',
        ),
        migrations.RemoveField(
            model_name='summonerpuuid',
            name='revisionDate',
        ),
        migrations.AddField(
            model_name='summonerpuuid',
            name='gameName',
            field=models.CharField(default='hide on bush', max_length=200),
        ),
        migrations.AddField(
            model_name='summonerpuuid',
            name='summonerId',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='summonerpuuid',
            name='tagLine',
            field=models.CharField(default='KR1', max_length=20),
        ),
        migrations.AlterField(
            model_name='summonerpuuid',
            name='accountId',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='summonerpuuid',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='summonerpuuid',
            name='profileIconId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='summonerpuuid',
            name='puuid',
            field=models.TextField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='summonerpuuid',
            name='summonerLevel',
            field=models.IntegerField(null=True),
        ),
    ]