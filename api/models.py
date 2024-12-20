from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

# Create your models here.
class Users(AbstractUser):
   profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    product_picture = models.ImageField(upload_to='product_picture/', blank=True, null=True)

class Orders(models.Model):
    name = models.CharField(max_length=255)
    OrderedBy = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='orders')
    orderDate = models.DateTimeField()
    
class Reviews(models.Model):
    pass