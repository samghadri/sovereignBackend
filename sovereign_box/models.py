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

    CERTIFICATION_TYPE = (
        ('P', "PCGS"),
        ('N', "NGC"),
    )

    name = models.CharField(max_length=100)

    metal_type = models.CharField(choices=COIN_OPTIONS, max_length=1)

    image = models.ImageField(
        upload_to="image_file/%Y/",
        blank=True, null=True, verbose_name="Image")

    image_2 = models.ImageField(
        upload_to="image_file/%Y/",
        blank=True, null=True, verbose_name="Image")

    year_of_mintage = models.CharField(max_length=60, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    grading_company = models.CharField(choices=CERTIFICATION_TYPE, max_length=1, blank=True, null=True)

    certification_code = models.CharField(max_length=30, blank=True, null=True)

    tags = models.ManyToManyField(
        CoinTag, through="CoinTagLink", blank=True)

    def __str__(self):
        return self.name


class CoinTagLink(models.Model):
    """Many to many link table for Newsletters and Reports"""

    coins = models.ForeignKey(Coins)
    coin_tag = models.ForeignKey(CoinTag)


class ContactUs(models.Model):

    full_name = models.CharField(max_length=100)

    email_address = models.CharField(max_length=150)

    description = models.TextField()

    def __str__(self):
        return self.full_name


class CoinOffer(models.Model):

    person = models.CharField(max_length=60)

    offer = models.CharField(max_length=60)

    coin = models.CharField(max_length=150)

    def __str__(self):
        return self.person
