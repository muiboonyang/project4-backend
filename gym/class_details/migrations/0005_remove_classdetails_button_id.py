# Generated by Django 4.0.1 on 2022-02-10 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_details', '0004_alter_classdetails_button_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classdetails',
            name='button_id',
        ),
    ]