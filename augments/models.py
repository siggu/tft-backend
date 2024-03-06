from django.db import models


# Create your models here.
class Augment(models.Model):
    """Model definition for Augments"""

    class TierChoices(models.TextChoices):
        SILVER = ("silver", "Silver")
        GOLD = ("gold", "Gold")
        PRISMATIC = ("prismatic", "Prismatic")

    tier = models.CharField(
        max_length=10,
        choices=TierChoices.choices,
        default="silver",
    )
    name = models.CharField(
        max_length=20,
    )
    description = models.CharField(
        max_length=200,
    )

    def __str__(self):
        return self.name
