from django.db import models


# Create your models here.
class Augment(models.Model):
    """Model definition for Augments"""

    key = models.CharField(
        max_length=20,
        primary_key=True,
        default="Eng_Key",
    )
    ingameKey = models.CharField(
        max_length=50,
        null=True,
    )
    name = models.CharField(max_length=20)
    desc = models.TextField(max_length=200)
    imageUrl = models.URLField(
        default="https://cdn.lolchess.gg/upload/images/items/ACutAbove_1685417489-A-Cut-Above-II.TFT_Set9.png"
    )
    isHidden = models.BooleanField(
        blank=True,
        null=True,
    )
    tier = models.PositiveIntegerField(default=1)
    championIngameKey = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    legendCode1 = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    legendCode2 = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    tag1 = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    tag2 = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
