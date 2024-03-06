from django.db import models


class Origin(models.Model):
    """Model Definition for Origins"""

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    champion = models.ManyToManyField(
        "champions.Champion",
        related_name="origins",
    )

    def __str__(self):
        return self.name


class Job(models.Model):
    """Model Definition for Lines"""

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    champion = models.ManyToManyField(
        "champions.Champion",
        related_name="jobs",
    )

    def __str__(self):
        return self.name
