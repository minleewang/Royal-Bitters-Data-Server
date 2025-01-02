from django.db import models

from wine.entity.wine import Wine


class WinePrice(models.Model):
    id = models.AutoField(primary_key=True)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name="prices")
    price = models.IntegerField()

    class Meta:
        db_table = 'wine_price'
        app_label = 'wine'

    def __str__(self):
        return f"Wine Price(id={self.id}, price={self.price})"

    def getPrice(self):
        return self.price