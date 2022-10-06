# Generated by Django 3.2.13 on 2022-07-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0009_delete_ledgermodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='LedgerModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('maiil_name', models.CharField(max_length=225)),
                ('mail_address', models.CharField(max_length=225)),
                ('mail_state', models.CharField(max_length=225)),
                ('mail_country', models.CharField(blank=True, max_length=225)),
                ('mail_pincode', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_details', models.CharField(default='Null', max_length=225)),
                ('pan_no', models.CharField(max_length=225)),
                ('registration_type', models.CharField(max_length=225)),
                ('gst_in', models.CharField(max_length=225)),
                ('alter_gst', models.CharField(max_length=225)),
            ],
        ),
    ]
