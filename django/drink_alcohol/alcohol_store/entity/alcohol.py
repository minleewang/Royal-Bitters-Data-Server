from django.db import models



# 술 이라면 용량에 대한 정보도 필요할것같음
# 술 roleType 으로 술의 종류 (whiskey, Beer, Wine)
# findByAlcohol로 카테고리별로 뽑을 수 있게 하셈

class Alcohol(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    #alcoholCategory = models.ForeignKey(AlcoholCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'alcohol'
        app_label = 'alcohol_store'

    def __str__(self):
        return f"alcohol(id={self.id}, title={self.title})"

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title