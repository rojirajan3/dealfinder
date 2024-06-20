from django.db import models


# Create your models here.

class RegisterDB(models.Model):
    UserId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class SellDB(models.Model):
    product = models.CharField(max_length=100, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    product_image = models.ImageField(upload_to="Profile", null=True, blank=True)
    UserId = models.ForeignKey(RegisterDB,blank=False,null=False, on_delete=models.CASCADE)

class ContactDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Feedback = models.CharField(max_length=100, null=True, blank=True)

