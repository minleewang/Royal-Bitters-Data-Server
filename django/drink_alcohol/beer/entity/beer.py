from django.db import models

from alcohol.entity.alcohol import Alcohol
from alcohol.entity.role_type import RoleType


class Beer(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    alcohol = models.ForeignKey(
        Alcohol,
        on_delete=models.CASCADE,
        related_name="beer_alcohols",
        #default=1000
        null=True,  # NULL 허용
        blank=True  # 폼에서 빈 값 허용
    )
    # Beer가 Alcohol을 ForgineKey로 가지고 있어야함.


    class Meta:
        db_table = 'beer'
        app_label = 'beer'

    def __str__(self):
        return f"Beer (id={self.id}, title={self.title})"

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title