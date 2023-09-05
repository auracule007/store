from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'img','slug', 'description']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'description', 'price', 'quantity', 'date_updated', 'date_uploaded']
admin.site.register(Product, ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message', 'sent', 'updated', 'status']
admin.site.register(Contact, ContactAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'firstName', 'lastName', 'pix','email', 'age', 'address']
admin.site.register(Profile, ProfileAdmin)

class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'name','quantity', 'price', 
    'amount', 'paid', 'order_no', 'added', 'updated']
admin.site.register(Shopcart, ShopcartAdmin)