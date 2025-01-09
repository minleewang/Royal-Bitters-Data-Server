from django.db import models

from beer.entity.beer import Beer


class BeerPrice(models.Model):
    id = models.AutoField(primary_key=True)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name="prices")
    price = models.IntegerField()

    class Meta:
        db_table = 'beer_price'
        app_label = 'beer'

    def __str__(self):
        return f"Beer Price(id={self.id}, price={self.price})"

    def getPrice(self):
        return self.price
