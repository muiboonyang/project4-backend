# Generated by Django 4.0.1 on 2022-02-05 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_details', '0009_alter_personaldetails_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]