from django.db import models

from alcohol.entity.alcohol_image import AlcoholImage
from alcohol.entity.role_type import RoleType


<<<<<<< Updated upstream
=======
# Alcohol 도메인을 도입하면 주류를 하나의 엔티티로 통합하여 관리할 수 있음.
# Alcohol 엔티티는 모든 주류(BEER, WHISKEY, WINE 등)의 공통 정보를 관리
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
    def getTitle(self):
        return self.title

    def getPrice(self):
        return self.price

    def getType(self):
        return self.type
=======
    def getAlcoholType(self):
        return self.type

    def getAlcoholTitle(self):
        return self.title

    def getAlcoholPrice(self):
        return self.price

    def getAlcoholImage(self):
        return self.image
>>>>>>> Stashed changes
