# Generated by Django 4.0.1 on 2022-02-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_review_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
