from tkinter import CASCADE
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    categories=models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.FloatField()
    image=models.ImageField(upload_to="Products")
    availability=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"

    def __str__(self):
        return self.name 
