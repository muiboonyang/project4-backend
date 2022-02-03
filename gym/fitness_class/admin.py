from django.contrib import admin
from .models import FitnessClass


class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('class_type', 'date_time', 'instructor', 'spot_one_booked', 'spot_two_booked', 'spot_three_booked')


# Register your models here.

admin.site.register(FitnessClass, FitnessClassAdmin)
