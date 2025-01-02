from django.db import models

from whiskey.entity.whiskey import Whiskey


class WhiskeyImage(models.Model):
    id = models.AutoField(primary_key=True)
    whiskey = models.ForeignKey(Whiskey, on_delete=models.CASCADE, related_name="images")
    image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'whiskey_image'
        app_label = 'whiskey'

    def __str__(self):
        return f"Whiskey Image(id={self.id}, image={self.image})"

    def getImage(self):
        return self.image