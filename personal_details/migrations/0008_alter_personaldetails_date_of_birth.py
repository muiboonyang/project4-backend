# Generated by Django 4.0.1 on 2022-02-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_details', '0007_alter_personaldetails_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='date_of_birth',
            field=models.DateField(default=''),
        ),
    ]
