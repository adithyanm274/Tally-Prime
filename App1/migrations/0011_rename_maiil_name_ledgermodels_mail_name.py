# Generated by Django 3.2.13 on 2022-07-21 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0010_ledgermodels'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ledgermodels',
            old_name='maiil_name',
            new_name='mail_name',
        ),
    ]
