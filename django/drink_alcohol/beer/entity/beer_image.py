from django.db import models

from beer.entity.beer import Beer


class BeerImage(models.Model):
    id = models.AutoField(primary_key=True)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name="images")
    image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'beer_image'
        app_label = 'beer'

    def __str__(self):
        return f"Beer Image(id={self.id}, image={self.image})"

    def getImage(self):
        return self.image