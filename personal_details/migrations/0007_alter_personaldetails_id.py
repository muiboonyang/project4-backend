# Generated by Django 4.0.1 on 2022-02-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_details', '0006_remove_personaldetails_emergency_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
