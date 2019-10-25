from django.db import models


class CoinTag(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Coins(models.Model):
    COIN_OPTIONS = (
        ('G', 'Gold'),
        ('S', 'Silver'),
        ('C', 'Copper')
    )

    name = models.CharField(max_length=100)

    metal_type = models.CharField(choices=COIN_OPTIONS, max_length=1)

    year_of_mintage = models.CharField(max_length=60, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    tags = models.ManyToManyField(
        CoinTag, through="CoinTagLink", blank=True)

    def __str__(self):
        return self.name


class CoinTagLink(models.Model):
    """Many to many link table for Newsletters and Reports"""

    coins = models.ForeignKey(Coins)
    coin_tag = models.ForeignKey(CoinTag)