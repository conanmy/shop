# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('date', models.DateField()),
                ('buyerName', models.CharField(max_length=100)),
                ('buyerEmail', models.CharField(max_length=100)),
                ('buyerPhoneNumber', models.CharField(max_length=100)),
                ('buyerAddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('productName', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('retailPrice', models.BigIntegerField()),
            ],
        ),
    ]