# Generated by Django 4.0.1 on 2022-02-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_class', '0003_alter_fitnessclass_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessclass',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
