from django.db import models


class Cars(models.Model):
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    concern = models.ForeignKey('Concern', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.model}'


class Concern(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ShopCar(models.Model):
    name = models.CharField(max_length=200)
    concerns = models.ManyToManyField(Concern)

    def __str__(self):
        return self.name


class Phone(models.Model):
    Brand = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    System = models.CharField(max_length=30)
    Display = models.DecimalField(max_digits=4, decimal_places=2)
    Price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'phone'


class Person(models.Model):
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    email = models.EmailField('Email')
    is_show = models.BooleanField('Показывать на странице', default=False)

    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class HomeWork(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='image/')
    file = models.FileField(upload_to='files/')


class ModelSlug(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)


class MyUser(models.Model):
    login = models.CharField(max_length=120)
    password = models.CharField(max_length=120)


"""КОРЗИНА"""


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='image/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name