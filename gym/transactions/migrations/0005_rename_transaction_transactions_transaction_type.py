# Generated by Django 4.0.1 on 2022-02-08 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_transactions_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='transaction',
            new_name='transaction_type',
        ),
    ]