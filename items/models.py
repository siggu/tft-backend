from django.db import models


class Item(models.Model):
    """Model definition for Items"""

    name = models.CharField(
        max_length=40,
    )
    description = models.TextField()
    effect = models.TextField(blank=True)

    generableItem = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ItemRecipe(models.Model):
    name = models.CharField(
        max_length=40,
    )
    element_item1 = models.ForeignKey(
        "Item",
        on_delete=models.CASCADE,
        null=True,
        related_name="element_item1",
    )
    element_item2 = models.ForeignKey(
        "Item",
        on_delete=models.CASCADE,
        null=True,
        related_name="element_item2",
    )
    result_item = models.ForeignKey(
        "Item",
        on_delete=models.CASCADE,
        null=True,
        related_name="result_item",
    )

    def __str__(self):
        return self.name
