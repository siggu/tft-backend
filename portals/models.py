from django.db import models


# Create your models here.
class Portal(models.Model):
    """Model definition for Portals"""

    name = models.CharField(
        max_length=30,
    )
    description = models.CharField(
        max_length=200,
    )
    portal_type = models.ForeignKey(
        "PortalType",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name


class PortalType(models.Model):
    class TypeChoices(models.TextChoices):
        CHAMP = ("champ", "Champ")
        COMBAT = ("combat", "Combat")
        SPATULA = ("spatula", "Spatula")
        COIN = ("coin", "Coin")
        CARD = ("card", "Card")
        ITEM = ("item", "Item")

    portal_type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        default="champ",
    )

    def __str__(self):
        return self.portal_type
