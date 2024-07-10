from django.db import models


class Comp(models.Model):
    """Model Definition for Comps"""

    name = models.CharField(max_length=30)
    elements = models.ManyToManyField(
        "CompElement",
        related_name="comp_element",
    )
    is_blind = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CompElement(models.Model):

    # 추천 메타의 각 챔피언 요소
    champion = models.ForeignKey(
        "champions.Champion",
        related_name="champion_comps",
        on_delete=models.CASCADE,
    )
    recommendedItem1 = models.ForeignKey(
        "items.Item",
        related_name="item_comps_1",
        blank="True",
        null="True",
        on_delete=models.CASCADE,
    )
    recommendedItem2 = models.ForeignKey(
        "items.Item",
        related_name="item_comps_2",
        null="True",
        blank="True",
        on_delete=models.CASCADE,
    )
    recommendedItem3 = models.ForeignKey(
        "items.Item",
        related_name="item_comps_3",
        null="True",
        blank="True",
        on_delete=models.CASCADE,
    )

    class CompChampionLevelChoice(models.IntegerChoices):
        oneStar = 1, "oneStar"
        twoStar = 2, "twoStar"
        threeStar = 3, "threeStar"

    championLevelChoice = models.IntegerField(
        choices=CompChampionLevelChoice.choices,
        default=CompChampionLevelChoice.twoStar,
    )

    def __str__(self):
        if self.recommendedItem1 and self.recommendedItem2 and self.recommendedItem3:
            return f"{self.champion.name} {'★'*self.championLevelChoice} ({self.recommendedItem1.name}+{self.recommendedItem2.name}+{self.recommendedItem3.name})"
        else:
            return f"{self.champion.name} {'★'*self.championLevelChoice} "

class MetaDecks(models.Model):
    name = models.CharField(max_length=100)
    decks = models.JSONField(
        "json",
        default=dict,
    )
class ItemUsage(models.Model):
    name = models.CharField(max_length=100)
    usages = models.JSONField(
        "json",
        default=dict,
    )