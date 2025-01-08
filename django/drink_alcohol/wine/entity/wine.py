from django.db import models

from alcohol.entity.alcohol import Alcohol
from alcohol.entity.role_type import RoleType


class Wine(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)


    def to_alcohol(self):
        # 연결된 데이터 조회
        price = self.price.first()  # Whiskey Price와 연결된 첫 번째 가격
        image = self.images.first()  # WhiskeyImage와 연결된 첫 번째 이미지

        # Alcohol 객체로 변환
        return Alcohol(
            id=self.id,
            type=RoleType.WINE.value,
            title=self.title,
            price=price.price if price else None,  # 가격이 없으면 None
            image=image.image if image else None,  # 이미지가 없으면 None
        )

    class Meta:
        db_table = 'wine'
        app_label = 'wine'

    def __str__(self):
        return f"Wine (id={self.id}, title={self.title})"

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title