from django.db import models

class Item(models.Model):
    """Model definition for Items"""

    name = models.CharField(
        max_length=40,
    )
    description = models.TextField(
    )
    effect = models.TextField(
        blank=True
    )

    generableItem = models.BooleanField(default = True)

    def __str__(self):
        return self.name