from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=32)

    class Meta:
        db_table = 'account'
        app_label = 'account'

    def getId(self):
        return self.id

    def getEmail(self):
        return self.email