from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    brand = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    guarantee = models.CharField(max_length=30)
    discount = models.PositiveIntegerField()
    material = models.CharField(max_length=30)
    rating = models.FloadField()
    stock = models.PositiveSmallIntegerField()