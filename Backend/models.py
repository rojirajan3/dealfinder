from django.db import models

# Create your models here.
class ProductDB(models.Model):
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Cat_Image = models.ImageField(upload_to="Profile", null=True, blank=True)