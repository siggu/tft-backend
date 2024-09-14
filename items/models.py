from django.db import models


class Set11Item(models.Model):
    """Model definition for Items"""

    key = models.CharField(max_length=100, default="Eng_Key")
    ingameKey = models.CharField(max_length=100, default="TFT_")
    ingameIcon = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    shortDesc = models.TextField(blank=True)
    fromDesc = models.TextField(blank=True)
    imageUrl = models.URLField()
    composition1 = models.CharField(blank=True, max_length=50)
    composition2 = models.CharField(blank=True, max_length=50)
    affectedTraitKey = models.CharField(max_length=20, blank=True)
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
    isHidden = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name


class Set12Item(models.Model):
    """Model definition for Items"""

    key = models.CharField(max_length=100, default="Eng_Key")
    ingameKey = models.CharField(max_length=100, default="TFT_")
    ingameIcon = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    shortDesc = models.TextField(blank=True)
    fromDesc = models.TextField(blank=True)
    imageUrl = models.URLField()
    composition1 = models.CharField(blank=True, max_length=50)
    composition2 = models.CharField(blank=True, max_length=50)
    affectedTraitKey = models.CharField(max_length=20, blank=True)
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
    isHidden = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name
