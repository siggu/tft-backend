from django.db import models


# Create your models here.
class Champion(models.Model):
    """Model Definition for Champions"""

    name = models.CharField(max_length=20)
    cost = models.PositiveIntegerField()
    synergies = models.ManyToManyField(
        "synergies.Synergy",
    )

    def __str__(self):
        return self.name
