from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Book(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category,related_name='books',on_delete=models.CASCADE)
    pages=models.IntegerField()
    price=models.IntegerField()
    description=models.TextField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-date_created']
        def __str__(self):
            return self.title

class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price=models.IntegerField()
    status=models.BooleanField(default=True)
    imageUrl=models.URLField()
    date_created=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-date_created']

    def __str__(self):
        return self.name

