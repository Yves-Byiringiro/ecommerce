from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    Name = models.CharField(max_length=250)
    Description = models.TextField()
    Image = models.ImageField(upload_to='products')
    Price = models.IntegerField()


    def __str__(self):
        return self.Name

class Watch(models.Model):
    Name = models.CharField(max_length=250)
    Description = models.TextField()
    Image = models.ImageField(upload_to='watches')
    Price = models.IntegerField()


    def __str__(self):
        return self.Name
