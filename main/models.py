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

        