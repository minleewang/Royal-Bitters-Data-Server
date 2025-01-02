from django.db import models

class Category(models.TextChoices):
    BEER = 'BEER'
    WINE = 'WINE'
    WHISKEY = 'WHISKEY'