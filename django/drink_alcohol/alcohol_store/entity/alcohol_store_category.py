from django.db import models

from alcohol_store.entity.alcohol import Alcohol
from alcohol_store.entity.store_category import Category


class AlcoholCategory(models.Model):
    id = models.AutoField(primary_key=True)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, related_name="categories")
    alcoholCategory = models.CharField(max_length=64, choices=Category.choices) #, default=StoreCategory.NORMAL)

    class Meta:
        db_table = 'alcohol_category'
        app_label = 'alcohol_store'


    def __str__(self):
        return f"alcoholCategory(id={self.id}, category={self.Category})"

    def getCategory(self):
        return self.alcoholCategory

