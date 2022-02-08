from django.contrib import admin
from .models import Transactions


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('classesPurchased', 'classesUsed', 'date', 'time', 'user', 'name')


# Register your models here.

admin.site.register(Transactions, TransactionsAdmin)
