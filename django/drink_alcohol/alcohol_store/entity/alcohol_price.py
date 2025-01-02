from django.db import models

from alcohol_store.entity.alcohol import Alcohol


class AlcoholPrice(models.Model):
    id = models.AutoField(primary_key=True)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, related_name="prices")
    price = models.IntegerField()

    class Meta:
        db_table = 'alcohol_price'
        app_label = 'alcohol_store'

    def __str__(self):
        return f"alcoholPrice(id={self.id}, price={self.price})"

    def getPrice(self):
        return self.price