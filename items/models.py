from django.db import models


class Item(models.Model):
    """Model definition for Items"""

    key = models.CharField(max_length=100, default="Eng_Key")
    ingameKey = models.CharField(max_length=100, default="TFT_")
    name = models.CharField(max_length=100)
    description = models.TextField()
    shortDesc = models.TextField(blank=True)
    imageUrl = models.URLField(
        default=""
    )
    composition1 = models.CharField(blank=True, max_length=50)
    composition2 = models.CharField(blank=True, max_length=50)
    isFromItem = models.BooleanField(
        blank=True,
        null=True,
    )
    isNormal = models.BooleanField(
        blank=True,
        null=True,
    )
    isEmblem = models.BooleanField(
        blank=True,
        null=True,
    )
    isSupport = models.BooleanField(
        blank=True,
        null=True,
    )
    isArtifact = models.BooleanField(
        blank=True,
        null=True,
    )
    isRadiant = models.BooleanField(
        blank=True,
        null=True,
    )
    isUnique = models.BooleanField(
        blank=True,
        null=True,
    )
    isNew = models.BooleanField(
        blank=True,
        null=True,
    )

    class TagChoice(models.TextChoices):
        # 태그 - 아이템 유형

        # 재료가 되는 기본 아이템
        FROMITEM = ("fromitem", "Fromitem")

        # 조합 가능한 아이템 (상징 미포함)
        NORMAL = ("normal", "Normal")

        # 상징
        EMBLEM = ("emblem", "Emblem")

        # 지원 아이템
        SUPPORT = ("support", "Support")

        # 오른 아이템
        ARTIFACT = ("artifact", "Artifact")

        # 찬란한 아이템
        RADIANT = ("radiant", "Radiant")

        # 고유 아이템
        UNIQUE = ("unique", "Unique")

        # 새로 나온 아이템
        NEW = ("new", "New")

    tag1 = models.TextField(
        choices=TagChoice.choices,
        blank=True,
        null=True,
    )
    tag2 = models.TextField(
        choices=TagChoice.choices,
        blank=True,
        null=True,
    )
    tag3 = models.TextField(
        choices=TagChoice.choices,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
