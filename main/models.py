from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    country = models.TextField(null=True, blank=True, max_length=30)
    content = models.TextField()
    data_p = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
