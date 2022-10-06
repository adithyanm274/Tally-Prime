# Generated by Django 3.2.13 on 2022-07-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crtcompony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componyname', models.CharField(max_length=50)),
                ('mailingname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=10)),
                ('telphone', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('fax', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=100)),
                ('fyearbgn', models.DateField()),
                ('booksbgn', models.DateField()),
                ('curncysymbl', models.CharField(max_length=10)),
                ('crncyname', models.CharField(max_length=10)),
            ],
        ),
    ]