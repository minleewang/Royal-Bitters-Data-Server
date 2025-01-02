from django.db import models

from alcohol_store.entity.alcohol import Alcohol


class AlcoholDescription(models.Model):
    id = models.AutoField(primary_key=True)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, related_name="descriptions")
    description = models.TextField()

    class Meta:
        db_table = 'alcohol_description'
        app_label = 'alcohol_store'

    def __str__(self):
        return f"alcoholDescription(id={self.id}, description={self.description})"

    def getDescription(self):
        return self.description