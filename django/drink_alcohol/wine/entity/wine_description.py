from django.db import models

from wine.entity.wine import Wine


class WineDescription(models.Model):
    id = models.AutoField(primary_key=True)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name="descriptions")
    description = models.TextField()

    class Meta:
        db_table = 'wine_description'
        app_label = 'wine'

    def __str__(self):
        return f"Wine Description(id={self.id}, description={self.description})"

    def getDescription(self):
        return self.description