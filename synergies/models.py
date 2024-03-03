from django.db import models


# Create your models here.
class Synergy(models.Model):
    """Model Definition for Synergies"""

    name = models.CharField(max_length=50)
    descriptoin = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Synergies"
