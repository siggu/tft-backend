from django.db import models


class Set11Champion(models.Model):
    """Model Definition for Champions"""

    key = models.CharField(
        max_length=20,
        primary_key=True,
        default="Eng_Key",
    )
    ingameKey = models.CharField(
        max_length=30,
        null=True,
    )
    name = models.CharField(max_length=20)
    imageUrl = models.URLField(
        default="//cdn.lolchess.gg/upload/images/champions/Aatrox_1709255107-Aatrox.jpg",
    )
    splashUrl = models.URLField(
        default="//cdn.lolchess.gg/upload/images/champion-splashes/Aatrox_18_1709256639-Aatrox.jpg"
    )
    traits1 = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    traits2 = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    traits3 = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    traits4 = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    isHiddenGuide = models.BooleanField(
        blank=True,
        null=True,
        default=False,
    )
    isHiddenLanding = models.BooleanField(
        blank=True,
        null=True,
        default=False,
    )
    isHiddenTeamBuiler = models.BooleanField(
        blank=True,
        null=True,
        default=False,
    )
    cost1 = models.IntegerField(default=1)
    cost2 = models.IntegerField(default=1)
    cost3 = models.IntegerField(default=1)
    health1 = models.PositiveIntegerField(default=1)
    health2 = models.PositiveIntegerField(default=1)
    health3 = models.PositiveIntegerField(default=1)
    attackDamage1 = models.PositiveIntegerField(default=1)
    attackDamage2 = models.PositiveIntegerField(default=1)
    attackDamage3 = models.PositiveIntegerField(default=1)
    damagePerSecond1 = models.PositiveIntegerField(default=1)
    damagePerSecond2 = models.PositiveIntegerField(default=1)
    damagePerSecond3 = models.PositiveIntegerField(default=1)
    attackRange = models.PositiveIntegerField(
        default=1,
    )
    attackSpeed = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=1,
    )
    armor = models.PositiveIntegerField(default=10)
    magicalResistance = models.PositiveIntegerField(default=10)
    recommendItems1 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    recommendItems2 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    recommendItems3 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    recommendItems4 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    recommendItems5 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    skill_name = models.CharField(max_length=20, default="스킬이름")
    skill_imageUrl = models.URLField(
        default="//cdn.lolchess.gg/upload/images/champion-skills/Aatrox_1709109373-aatrox_q.png"
    )
    skill_desc = models.TextField(max_length=500, default="스킬 설명")
    skill_startingMana = models.PositiveIntegerField(default=10)
    skill_skillMana = models.PositiveIntegerField(default=10)
    skill_stats1 = models.TextField(blank=True, null=True)
    skill_stats2 = models.TextField(blank=True, null=True)
    skill_stats3 = models.TextField(blank=True, null=True)
    skill_stats4 = models.TextField(blank=True, null=True)
    skill_stats5 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Set12Champion(models.Model):
    """Model Definition for Champions"""

    key = models.CharField(
        max_length=20,
        primary_key=True,
        default="Eng_Key",
    )
    ingameKey = models.CharField(
        max_length=30,
        null=True,
    )
    name = models.CharField(max_length=20)
    imageUrl = models.URLField(
        default="//cdn.lolchess.gg/upload/images/champions/Aatrox_1709255107-Aatrox.jpg",
    )
    splashUrl = models.URLField(
        default="//cdn.lolchess.gg/upload/images/champion-splashes/Aatrox_18_1709256639-Aatrox.jpg"
    )
    traits1 = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    traits2 = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    traits3 = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    traits4 = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    isHiddenGuide = models.BooleanField(
        blank=True,
        null=True,
        default=False,
    )
    isHiddenLanding = models.BooleanField(
        blank=True,
        null=True,
        default=False,
    )
    isHiddenTeamBuiler = models.BooleanField(
        blank=True,
        null=True,
        default=False,
    )
    cost1 = models.IntegerField(default=1)
    cost2 = models.IntegerField(default=1)
    cost3 = models.IntegerField(default=1)
    health1 = models.PositiveIntegerField(default=1)
    health2 = models.PositiveIntegerField(default=1)
    health3 = models.PositiveIntegerField(default=1)
    attackDamage1 = models.PositiveIntegerField(default=1)
    attackDamage2 = models.PositiveIntegerField(default=1)
    attackDamage3 = models.PositiveIntegerField(default=1)
    damagePerSecond1 = models.PositiveIntegerField(default=1)
    damagePerSecond2 = models.PositiveIntegerField(default=1)
    damagePerSecond3 = models.PositiveIntegerField(default=1)
    attackRange = models.PositiveIntegerField(
        default=1,
    )
    attackSpeed = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=1,
    )
    armor = models.PositiveIntegerField(default=10)
    magicalResistance = models.PositiveIntegerField(default=10)
    recommendItems1 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    recommendItems2 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    recommendItems3 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    recommendItems4 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    recommendItems5 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    skill_name = models.CharField(max_length=20, default="스킬이름")
    skill_imageUrl = models.URLField(
        default="//cdn.lolchess.gg/upload/images/champion-skills/Aatrox_1709109373-aatrox_q.png"
    )
    skill_desc = models.TextField(max_length=500, default="스킬 설명")
    skill_startingMana = models.PositiveIntegerField(default=10)
    skill_skillMana = models.PositiveIntegerField(default=10)
    skill_stats1 = models.TextField(blank=True, null=True)
    skill_stats2 = models.TextField(blank=True, null=True)
    skill_stats3 = models.TextField(blank=True, null=True)
    skill_stats4 = models.TextField(blank=True, null=True)
    skill_stats5 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name