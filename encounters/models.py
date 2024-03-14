from django.db import models


# Create your models here.
class Encounter(models.Model):
    name = models.CharField(max_length=10)
    description_1 = models.TextField(
        max_length=200,
        blank=True,
    )
    description_2 = models.TextField(
        max_length=200,
        blank=True,
    )
    description_3 = models.TextField(
        max_length=200,
        blank=True,
    )
    description_4 = models.TextField(
        max_length=200,
        blank=True,
    )

    def __str__(self):
        return self.name
