# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inputPerson_id', models.IntegerField()),
                ('inputDate', models.DateField()),
                ('newProduct', models.CharField(max_length=100)),
                ('branchShop_id', models.IntegerField(default=None, null=True)),
                ('productNo', models.CharField(max_length=100)),
                ('productName', models.CharField(max_length=100)),
                ('unitPrice', models.BigIntegerField()),
                ('retailPrice', models.BigIntegerField()),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('discountEnable', models.CharField(max_length=100)),
                ('discountPercent', models.BigIntegerField()),
                ('wholesalesPrice', models.BigIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('productPicture1', models.CharField(max_length=100)),
                ('productPicture2', models.CharField(max_length=100)),
                ('productPicture3', models.CharField(max_length=100)),
            ],
        ),
    ]
