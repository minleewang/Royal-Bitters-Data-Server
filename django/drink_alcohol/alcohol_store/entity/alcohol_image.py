from django.db import models

from alcohol_store.entity.alcohol import Alcohol


class AlcoholImage(models.Model):
    id = models.AutoField(primary_key=True)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, related_name="images")
    image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'alcohol_image'
        app_label = 'alcohol_store'

    def __str__(self):
        return f"alcoholImage(id={self.id}, image={self.image})"

    def getImage(self):
        return self.image