# Generated by Django 4.0.1 on 2022-02-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transactions_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='transaction',
            field=models.CharField(default='', max_length=20),
        ),
    ]
