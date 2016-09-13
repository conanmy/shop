from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    inputPerson_id = models.IntegerField()
    inputDate = models.DateField()
    newProduct = models.CharField(max_length=100)
    branchShop_id = models.IntegerField(default=None, null=True)
    productNo = models.CharField(max_length=100)
    productName = models.CharField(max_length=100)
    unitPrice = models.BigIntegerField()
    retailPrice = models.BigIntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    discountEnable = models.CharField(max_length=100)
    discountPercent = models.BigIntegerField()
    wholesalesPrice = models.BigIntegerField()
    location = models.CharField(max_length=100)
    productPicture1 = models.CharField(max_length=100)
    productPicture2 = models.CharField(max_length=100)
    productPicture3 = models.CharField(max_length=100)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    date = models.DateField()
    buyerName = models.CharField(max_length=100)
    buyerEmail = models.CharField(max_length=100)
    buyerPhoneNumber = models.CharField(max_length=100)
    buyerAddress = models.CharField(max_length=100)

class Record(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    productName = models.CharField(max_length=100)
    quantity = models.IntegerField()
    retailPrice = models.BigIntegerField()