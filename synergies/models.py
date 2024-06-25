from django.db import models


class Trait(models.Model):
    """Model Definition for Lines"""

    key = models.CharField(
        max_length=20,
        primary_key=True,
    )
    ingameKey = models.CharField(max_length=40)
    name = models.CharField(max_length=20)
    desc = models.TextField(
        max_length=300,
        blank=True,
    )
    imageUrl = models.URLField(
        default="https://cdn.lolchess.gg/upload/images/traits/Arcanist_normal_1709371622-arcanist.svg"
    )
    blackImageUrl = models.URLField(
        default="https://cdn.lolchess.gg/upload/images/traits/Arcanist_black_1709371622-arcanist.svg"
    )
    whiteImageUrl = models.URLField(
        default="https://cdn.lolchess.gg/upload/images/traits/Arcanist_white_1709371623-arcanist.svg"
    )
    _type = models.CharField(max_length=6)
    style1 = models.CharField(max_length=10)
    style1_min = models.PositiveIntegerField(default=1)
    style1_max = models.PositiveIntegerField(
        default=1,
        blank=True,
        null=True,
    )
    style2 = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    style2_min = models.PositiveIntegerField(
        default=1,
        blank=True,
        null=True,
    )
    style2_max = models.PositiveIntegerField(
        default=1,
        blank=True,
        null=True,
    )
    style3 = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    style3_min = models.PositiveIntegerField(
        default=1,
        blank=True,
        null=True,
    )
    style3_max = models.PositiveIntegerField(
        default=1,
        blank=True,
        null=True,
    )
    style4 = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    style4_min = models.PositiveIntegerField(
        default=1,
        blank=True,
        null=True,
    )
    stats1 = models.TextField(
        max_length=200,
        blank=True,
        null=True,
    )
    stats2 = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    stats3 = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    stats4 = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    stats5 = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    stats6 = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
