# Generated by Django 4.0.1 on 2022-02-09 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_rename_classespurchased_transactions_classcredit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='time',
            field=models.TimeField(verbose_name='15:18:13'),
        ),
    ]
