from django.db import models


# Create your models here.
class Portal(models.Model):
    """Model definition for Portals"""

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
    name = models.CharField(
        max_length=30,
    )
    description = models.CharField(
        max_length=200,
    )
    image = models.ImageField(
        null=True,
    )

    def __str__(self):
        return self.name
