from django.db import models


# Create your models here.
class Photo(models.Model):
    file = models.URLField()
    description = models.CharField(
        max_length=140,
    )
    portal = models.ForeignKey(
        "portals.PortalType",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    encounter = models.ForeignKey(
        "encounters.Encounter",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    # compElement = models.ForeignKey(
    #     "comp.CompElement",
    #     null=True,
    #     blank=True,
    #     on_delete=models.CASCADE,
    #     related_name="photos",
    # )

    def __str__(self):
        return self.description
