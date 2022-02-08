from django.db import models
import datetime
from django.conf import settings


User = settings.AUTH_USER_MODEL


# Create your models here.

class Transactions(models.Model):

    classesPurchased = models.IntegerField(default=0)
    classesUsed = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default="")
    user = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    @property
    def balance(self):
        return self.classesPurchased - self.classesUsed

    def _str_(self):
        return self.user


