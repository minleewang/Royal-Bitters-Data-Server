from django.db import models

from whiskey.entity.whiskey import Whiskey


class WhiskeyPrice(models.Model):
    id = models.AutoField(primary_key=True)
    whiskey = models.ForeignKey(Whiskey, on_delete=models.CASCADE, related_name="prices")
    price = models.IntegerField()

    class Meta:
        db_table = 'whiskey_price'
        app_label = 'whiskey'

    def __str__(self):
        return f"Whiskey Price(id={self.id}, price={self.price})"

    def getPrice(self):
        return self.price