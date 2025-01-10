from django.db import models

from alcohol.entity.alcohol import Alcohol
from alcohol.entity.role_type import RoleType


class Whiskey(models.Model):
    id = models.AutoField(primary_key=True)
    alcohol = models.ForeignKey(
        Alcohol,
        on_delete=models.CASCADE,
        related_name="whiskey_alcohols",
        #default=1000
        null=True,  # NULL 허용
        blank=True  # 폼에서 빈 값 허용
    )


    class Meta:
        db_table = 'whiskey'
        app_label = 'whiskey'

    def __str__(self):
        return f"Whiskey (id={self.id})"

    def getId(self):
        return self.id

    def getAlcohol(self):
        return self.alcohol