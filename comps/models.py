from django.db import models


class Comp(models.Model):
    """Model Definition for Comps"""

    name = models.CharField(max_length=30)
    champions = models.ManyToManyField(
        "champions.Champion",
        related_name="comps",
    )

    def __str__(self):
        return self.name
