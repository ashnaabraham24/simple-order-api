from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100) #stores basic user information

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)#stores product details 
    price = models.DecimalField(max_digits=10, decimal_places=2) #Price of the product

    def __str__(self):
        return self.name
    
#order placed by a user for a product
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user} ordered {self.product} ({self.quantity})"
