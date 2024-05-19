# models.py
from django.db import models


class Comp(models.Model):
    teamBuilderKey = models.CharField(
        max_length=40, default="ac80267f71bc9386e411b92ed7cb9b5c6287be80"
    )
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=20, blank=True, null=True)
    cost = models.IntegerField(default=1)
    augments = models.JSONField(blank=True, null=True)
    season = models.CharField(max_length=10, default=10)
    set = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class CompElement(models.Model):
    comp = models.ForeignKey(Comp, related_name="elements", on_delete=models.CASCADE)
    index = models.IntegerField()
    champion = models.CharField(max_length=100)
    star = models.IntegerField(default=1)
    items = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.champion} - {self.star}★"
