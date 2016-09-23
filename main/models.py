from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)
    buyerName = models.CharField(max_length=100)
    buyerEmail = models.CharField(max_length=100)
    buyerPhoneNumber = models.CharField(max_length=100)
    buyerAddress = models.CharField(max_length=100)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(User, through='Cart')
    order = models.ManyToManyField(Order, through='Record')
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


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    productName = models.CharField(max_length=100)
    quantity = models.IntegerField()
    retailPrice = models.BigIntegerField()