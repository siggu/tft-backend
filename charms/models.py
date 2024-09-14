from django.db import models

# Create your models here.
class Set12Charm(models.Model):
    """Model definition for Charms"""

    name = models.CharField(max_length=30)
    cost = models.IntegerField()
    tier = models.DecimalField(max_digits=3, decimal_places=1)
    _key = models.CharField(
        max_length=100,
    )
    desc = models.TextField(
        max_length=300,
        default="",
    )
    imageUrl = models.URLField(
        default="https://cdn.dak.gg/tft/images2/charms/set12/charm-1.png"
    )

    def __str__(self):
        return self.name
