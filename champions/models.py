from django.db import models


class Champion(models.Model):
    """Model Definition for Champions"""

    name = models.CharField(max_length=20)
    cost = models.PositiveIntegerField()
    origin = models.ManyToManyField(
        "synergies.Origin",
        related_name="champions",
    )
    job = models.ManyToManyField(
        "synergies.Job",
        related_name="champions",
    )
    health = models.PositiveIntegerField(
        default=100,
    )
    ad = models.PositiveIntegerField(
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
    armor = models.PositiveIntegerField(
        default=10,
    )
    magic_resistance = models.PositiveIntegerField(
        default=10,
    )
    skill = models.ForeignKey(
        "Skill",
        on_delete=models.CASCADE,
        null=True,
    )

    @property
    def dps(self):
        return self.ad * float(self.attack_speed)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Model Definition for Skill"""

    class TypeChoices(models.TextChoices):
        ACTIVE = ("active", "Active")
        PASSIVE = ("passive", "Passive")

    name = models.CharField(
        max_length=50,
    )
    skill_type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
    )
    start_mana = models.PositiveIntegerField(
        null=True,
    )
    max_mana = models.PositiveIntegerField(
        null=True,
    )
    description = models.TextField(default='스킬설명입력')
    effect = models.TextField(default='스킬효과입력')

    def __str__(self):
        return self.name
