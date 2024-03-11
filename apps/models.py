from django.db import models
import uuid


class Product(models.Model):
    name = models.CharField(max_length=128)
    product_code = models.CharField(max_length=128, unique=True)
    qty = models.IntegerField()

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.FloatField()


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='W_materials')
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.material} - qolgan: {self.remainder} - narxi:{self.price} dan"
