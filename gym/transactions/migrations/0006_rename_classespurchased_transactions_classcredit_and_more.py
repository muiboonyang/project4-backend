# Generated by Django 4.0.1 on 2022-02-08 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_rename_transaction_transactions_transaction_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='classesPurchased',
            new_name='classCredit',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='classesUsed',
            new_name='classDebit',
        ),
    ]
