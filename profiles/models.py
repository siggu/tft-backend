# models.py

from django.db import models


class SummonerPuuid(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    accountId = models.CharField(max_length=100)
    puuid = models.CharField(max_length=100)
    name = models.CharField(max_length=30, default="소환사닉네임")
    profileIconId = models.PositiveIntegerField(default=0)
    revisionDate = models.PositiveIntegerField(default=0)
    summonerLevel = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
