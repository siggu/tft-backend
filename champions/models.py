from django.db import models


# Create your models here.
class Champion(models.Model):
    """Model Definition for Champions"""

    name = models.CharField(max_length=20)
    cost = models.PositiveIntegerField()
    synergies = models.ManyToManyField(
        "synergies.Synergy",
    )
    health = models.PositiveIntegerField(
        default=100,
    )
    offense_power = models.PositiveIntegerField(
        default=10,
    )
    dps = models.PositiveIntegerField(
        default=10,
    )
    attack_range = models.PositiveIntegerField(
        default=1,
    )
    attack_speed = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=1,
    )
    defense = models.PositiveIntegerField(
        default=10,
    )
    magic_resistance = models.PositiveIntegerField(
        default=10,
    )
    avatar = models.ImageField(null=True)

    def __str__(self):
        return self.name
