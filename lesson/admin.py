from django.contrib import admin

from .models import Cars, Phone, Concern, ShopCar, Person, ModelSlug

admin.site.register(Cars)
admin.site.register(Phone)
admin.site.register(Concern)
admin.site.register(ShopCar)
admin.site.register(Person)
admin.site.register(ModelSlug)



from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)