from django.contrib import admin
from .models import Category,Book,Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Product)