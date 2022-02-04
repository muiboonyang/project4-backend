# Generated by Django 4.0.1 on 2022-02-04 13:43

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_details', '0002_personaldetails_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='address_line',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='contact',
            field=models.CharField(default='', max_length=8, validators=[django.core.validators.RegexValidator(regex='[6,8,9]\\d\\d\\d\\d\\d\\d\\d')]),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='emergency_contact',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='emergency_number',
            field=models.CharField(default='', max_length=8, validators=[django.core.validators.RegexValidator(regex='[6,8,9]\\d\\d\\d\\d\\d\\d\\d')]),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='gender',
            field=models.CharField(default='Male', max_length=10),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='postal_code',
            field=models.CharField(default='', max_length=10),
        ),
    ]
