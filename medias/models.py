from django.db import models


# Create your models here.
class Photo(models.Model):
    file = models.URLField()
    description = models.CharField(
        max_length=140,
    )
    augment = models.ForeignKey(
        "augments.Augment",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    champion = models.ForeignKey(
        "champions.Champion",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    skill = models.ForeignKey(
        "champions.Skill",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    portal = models.ForeignKey(
        "portals.Portal",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    origin = models.ForeignKey(
        "synergies.Origin",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    job = models.ForeignKey(
        "synergies.Job",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    item = models.ForeignKey(
        "items.Item",
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

    def __str__(self):
        return self.description
