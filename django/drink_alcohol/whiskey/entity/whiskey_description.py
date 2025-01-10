from django.db import models
from whiskey.entity.whiskey import Whiskey


class WhiskeyDescription(models.Model):
    id = models.AutoField(primary_key=True)
    whiskey = models.ForeignKey(Whiskey, on_delete=models.CASCADE, related_name="descriptions")
    description = models.TextField()

    class Meta:
        db_table = 'whiskey_description'
        app_label = 'whiskey'

    def __str__(self):
        return f"Whiskey Description(id={self.id}, description={self.description})"

    def getDescription(self):
        return self.description