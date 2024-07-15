from django.db import models


# Create your models here.
class Set11Portal(models.Model):
    """Model definition for Portals"""

    _type = models.CharField(
        max_length=10,
        default="Augments",
    )
    _key = models.CharField(
        max_length=100,
        default="TFT_Portals_Augments_GoldThird",
    )
    title = models.CharField(max_length=30)
    desc = models.TextField(
        max_length=300,
        default="이번 게임에서 얻는 마지막 증강이 골드 티어가 됩니다.",
    )
    iconImageUrl = models.URLField(
        default="https://s-tft-api.op.gg/img/set/11/tft-region-portal/augmentcards_icon.png"
    )

    def __str__(self):
        return self.title

class Set12Portal(models.Model):
    """Model definition for Portals"""

    _type = models.CharField(
        max_length=10,
        default="Augments",
    )
    _key = models.CharField(
        max_length=100,
        default="TFT_Portals_Augments_GoldThird",
    )
    title = models.CharField(max_length=30)
    desc = models.TextField(
        max_length=300,
        default="이번 게임에서 얻는 마지막 증강이 골드 티어가 됩니다.",
    )
    iconImageUrl = models.URLField(
        default="https://s-tft-api.op.gg/img/set/11/tft-region-portal/augmentcards_icon.png"
    )

    def __str__(self):
        return self.title
