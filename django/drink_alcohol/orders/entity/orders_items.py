from django.db import models

from alcohol.entity.alcohol import Alcohol
#from game_software.entity.game_software import GameSoftware
from orders.entity.orders import Orders


class OrdersItems(models.Model):
    id = models.AutoField(primary_key=True)
    orders = models.ForeignKey(Orders, related_name="items", on_delete=models.CASCADE)  # Order와 연결
    #game_software = models.ForeignKey(GameSoftware, related_name="items", on_delete=models.CASCADE)
    alcohol = models.ForeignKey(Alcohol, related_name="items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item: {self.quantity} x {self.price}"

    class Meta:
        db_table = 'orders_items'
        app_label = 'orders'