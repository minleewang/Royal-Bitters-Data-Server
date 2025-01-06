from django.db import models

# Create your models here.
class AlcoholImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'alcohol_image'
        app_label = 'alcohol'


    def getImage(self):
        return self.image