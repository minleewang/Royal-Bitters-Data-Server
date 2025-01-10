from django.db import models

from alcohol.entity.alcohol import Alcohol
from alcohol.entity.role_type import RoleType


class Wine(models.Model):
    id = models.AutoField(primary_key=True)
    alcohol = models.ForeignKey(
        Alcohol,
        on_delete=models.CASCADE,
        related_name="wine_alcohols",
        #default=1000
        null=True,  # NULL 허용
        blank=True  # 폼에서 빈 값 허용
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