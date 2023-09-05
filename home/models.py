from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    img = models.ImageField(default='category.jpg', upload_to='Category')
    description = models.TextField(default='')

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length= 50)
    slug = models.SlugField(default='')
    img = models.ImageField(default='product.jpg', upload_to='Product')
    description =models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    date_updated = models.DateField(auto_now=True)
    date_uploaded = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    STATUS = [
        ('New', 'New'),
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default='New')
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    pix = models.ImageField(upload_to="Profile", default= "profile.jpg")
    phone_no = models.CharField(max_length=50, default='+234')
    age = models.CharField(max_length=12)
    address = models.TextField()
    
    def __str__(self):
        return self.user.username 


class Shopcart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    amount = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    order_no = models.CharField(max_length=255)
    added = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name 

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    amount = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    order_no = models.CharField(max_length=255)
    added = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name 
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    amount = models.CharField(max_length=50)
    paid = models.BooleanField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200, default='')
    shop_code = models.CharField(max_length=50)
    pay_code = models.CharField(max_length=50)
    pay_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username 
    