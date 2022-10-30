from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from carcollection.carcollection_app.validators import Between1980_2049Validator


# Create your models here.


class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MAX_LEN_PASSWORD = 30
    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_USERNAME,
        validators=[MinLengthValidator(2, message='The username must be a minimum of 2 chars'), ]
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(18), ]
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_PASSWORD,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    profile_picture = models.URLField(
        null=False,
        blank=False,
    )


class Car(models.Model):
    TYPE_CHOICES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices=TYPE_CHOICES,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(MinLengthValidator(2), ),
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(Between1980_2049Validator, )
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(1), )
    )
