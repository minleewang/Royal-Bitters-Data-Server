from django.db import models

from wine.entity.wine import Wine


class WineImage(models.Model):
    id = models.AutoField(primary_key=True)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name="images")
    image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'wine_image'
        app_label = 'wine'

    def __str__(self):
        return f"Wine Image(id={self.id}, image={self.image})"

    def getImage(self):
        return self.image