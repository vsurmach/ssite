from django.shortcuts import render

from .models import News, Product, Category


# def index(request):
#     news = News.objects.all()
#     context = {'news': news}
#     return render(request, "index.html", context)
#
def index(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'category': category
               }
    return render(request, "index.html", context)


def get_category(request, id):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context = {'products': products, 'category': category
               }
    return render(request, "index.html", context)