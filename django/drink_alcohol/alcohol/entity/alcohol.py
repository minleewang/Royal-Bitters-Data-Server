from django.db import models

from alcohol.entity.alcohol_image import AlcoholImage
from alcohol.entity.role_type import RoleType


class Alcohol(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.IntegerField()
    image = models.ForeignKey(AlcoholImage, on_delete=models.CASCADE, related_name="images")
    type = models.CharField(
        max_length=15,
        choices=[(role.value, role.name) for role in RoleType],
    )

    class Meta:
        db_table = 'alcohol'
        app_label = 'alcohol'


    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getPrice(self):
        return self.price

    def getType(self):
        return self.type