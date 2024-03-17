from django.db import models


class Item(models.Model):
    """Model definition for Items"""

    key = models.CharField(max_length=40, default="Eng_Key")

    name = models.CharField(max_length=40)
    inGameKey = models.CharField(max_length=40, default="TFT_")
    description = models.TextField()
    effect = models.TextField(blank=True)

    generableItem = models.BooleanField(default=True)

    composition1 = models.CharField(blank=True, max_length=50)
    composition2 = models.CharField(blank=True, max_length=50)

    class TagChoice(models.TextChoices):
        # 태그 - 아이템 유형

        # 재료가 되는 기본 아이템
        BASIC = ("basic", "Basic")

        # 조합 가능한 아이템 (상징 미포함)
        NORMAL = ("normal", "Normal")

        # 상징
        EMBLEM = ("emblem", "Emblem")

        # 지원 아이템
        SUPPORT = ("support", "Support")

        # 오른 아이템
        ARTIFAC = ("artifact", "Artifact")

        # 찬란한 아이템
        RADIANT = ("radiant", "Radiant")

        # 기타 아이템
        ETC = ("etc", "Etc")

    tags = models.TextField(choices=TagChoice.choices, default="Normal")

    imageUrl = models.URLField(
        default="https://ih1.redbubble.net/image.2477120866.6033/raf,750x1000,075,t,101010:01c5ca27c6.u1.jpg",
    )

    def __str__(self):
        return self.name
