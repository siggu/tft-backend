from django.db import models


# Create your models here.
class Encounter(models.Model):

    # apiName 조우자 api 이름 PK
    ingameKey = models.CharField(
        primary_key=True,
        max_length=70,
        default="inGameKey",
    )

    # encounterDesc 조우자 효과 설명 (desc보다 자세한 설명임)
    encounterDesc = models.TextField(
        max_length=1000,
        default="조우자 설명",
    )

    # title 챔피언 이름 한글로
    name = models.CharField(max_length=20)

    # tileImageUrl 와꾸 이미지
    tileImageUrl = models.URLField(
        default="//cdn.lolchess.gg/upload/images/champions/Aatrox_1709255107-Aatrox.jpg",
    )

    def __str__(self):
        return self.name
