from django.db import models


class Origin(models.Model):
    """Model Definition for Origins"""

    name = models.CharField(max_length=50)
    description = models.TextField()
    effect_1 = models.TextField(blank=True, null=True)
    effect_2 = models.TextField(blank=True, null=True)
    effect_3 = models.TextField(blank=True, null=True)
    effect_4 = models.TextField(blank=True, null=True)
    effect_5 = models.TextField(blank=True, null=True)
    effect_6 = models.TextField(blank=True, null=True)
    tier = models.ForeignKey(
        "SynergyTier",
        on_delete=models.CASCADE,
        null=True,
    )
    stack = models.ForeignKey(
        "SynergyStack",
        on_delete=models.CASCADE,
        null=True,
    )
    # champion = models.ManyToManyField(
    #     "champions.Champion",
    #     related_name="origins",
    # )

    def __str__(self):
        return self.name


class Job(models.Model):
    """Model Definition for Lines"""

    name = models.CharField(max_length=50)
    description = models.TextField()
    effect_1 = models.TextField(blank=True, null=True)
    effect_2 = models.TextField(blank=True, null=True)
    effect_3 = models.TextField(blank=True, null=True)
    effect_4 = models.TextField(blank=True, null=True)
    tier = models.ForeignKey(
        "SynergyTier",
        on_delete=models.CASCADE,
        null=True,
    )
    stack = models.ForeignKey(
        "SynergyStack",
        on_delete=models.CASCADE,
        null=True,
    )
    # champion = models.ManyToManyField(
    #     "champions.Champion",
    #     related_name="jobs",
    # )

    def __str__(self):
        return self.name


class SynergyTier(models.Model):
    class TierChoices(models.TextChoices):
        BSG = ("b/s/g", "B/S/G")
        BGP = ("b/g/p", "B/G/P")
        BSGP = ("b/s/g/p", "B/S/G/P")
        BSSSGG = ("b/s/s/s/g/g", "B/S/S/G/G")
        BG = ("b/g", "B/G")
        UNIQUE = ("unique", "UNIQUE")
        NONE = ("none", "NONE")

    name = models.CharField(
        max_length=20,
        choices=TierChoices.choices,
    )

    def __str__(self):
        return self.name


class SynergyStack(models.Model):
    class StackChoices(models.TextChoices):
        one = ("1", "1")
        two_four = ("2/4", "2/4")
        two_three_four = ("2/3/4", "2/3/4")
        two_three_four_five = ("2/3/4/5", "2/3/4/5")
        two_four_six = ("2/4/6", "2/4/6")
        two_four_six_eight = ("2/4/6/8", "2/4/6/8")
        two_three_four_five_six_seven = ("2/3/4/5/6/7", "2/3/4/5/6/7")
        three_five = ("3/5", "3/5")
        three_five_seven = ("3/5/7", "3/5/7")
        three_five_seven_ten = ("3/5/7/10", "3/5/7/10")

    stack = models.CharField(
        max_length=30,
        choices=StackChoices.choices,
    )

    def __str__(self):
        return self.stack
