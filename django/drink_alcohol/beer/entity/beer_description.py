from django.db import models

from beer.entity.beer import Beer


class BeerDescription(models.Model):
    id = models.AutoField(primary_key=True)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name="descriptions")
    description  = models.TextField()

    class Meta:
        db_table = 'beer_description'
        app_label = 'beer'

    def __str__(self):
        return f"Beer Description(id={self.id}, description={self.description})"

    def getDescription(self):
        return self.description