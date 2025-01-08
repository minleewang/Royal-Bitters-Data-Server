from django.db import models
from account.entity.account import Account
from alcohol.entity.alcohol import Alcohol


class Cart(models.Model):

    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="carts")
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, related_name="cart_entries")
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cart'
        app_label = 'cart'


    def __str__(self):
        return (f"Cart(id={self.id}, "
                f"account={self.account}, "
                f"alcohol={self.alcohol}),"
                f"quantity={self.quantity}")


    def getId(self):
        return self.id

    def getAccount(self):
        return self.account

    def getAlcohol(self):
        return self.alcohol

    def getQuantity(self):
        return self.quantity