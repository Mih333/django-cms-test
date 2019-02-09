from django.db import models
from django.urls import reverse

# Create your models here.


class TextureOption(models.Model):
    texture_option = models.ImageField(upload_to='uploads/')


class TextureChoice(models.Model):
    position_choice = (
        ('TOP', 'Top'),
        ('BOTTOM', 'Bottom'),
        ('BACK', 'Back'),
        ('NECK', 'Neck'),
    )

    position = models.CharField(choices=position_choice, max_length=6)
    option = models.ForeignKey(TextureOption)


class Item(models.Model):

    name = models.CharField(max_length=255)
    price = models.IntegerField()
