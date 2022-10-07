from django.http import HttpResponse
from django.shortcuts import render
import sqlite3

from django.views.generic import CreateView

from .forms import PersonForm, PrForm, HomeworkForm, MyUserForm
from .models import Cars, Phone, Concern, Person, HomeWork, Product, Category
from .stor import fn


def get_car(request):
    # car = Cars.objects.all()
    context = {'cars': fn()}
    return render(request, 'car.html', context)


def get_phone(request):
    phone = Phone.objects.all()
    context = {'phone': phone}
    return render(request, 'phone.html', context)


def get_fk_car(request):
    if request.method == 'POST':
        down_wind = request.POST.get('select')
        search = request.POST.get('poisk')
        if down_wind == 'brand':
            main = Cars.objects.select_related('concern').filter(brand=search)
        elif down_wind == 'concern':
            main = Cars.objects.select_related('concern').filter(concern__title=search)
        elif down_wind == 'shop':
            main = Cars.objects.prefetch_related('concern__shop_car').filter(concern__shopcar__name=search)

        context = {'main': main}
        return render(request, 'result.html', context)

    return render(request, 'fk_car.html')


l = 'Alex'
p = "123"


# def login_1(request):
#     if request.method == "POST":
#         if l == request.POST.get('login') and p == request.POST.get('password'):
#             return HttpResponse('Вы вошли в кабинет')
#         else:
#             context = {'error': 'Неверный логин или пароль'}
#             return render(request, )


def add_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        person = Person.objects.create(name=name, surname=surname, email=email)
        context = {'success': 'Успешно сохранено'}
        return render(request, 'person.html', context)
    return render(request, 'person.html')


def person_list(request):
    chel = Person.objects.filter(is_show=True)
    context = {'chel': chel}
    return render(request, 'person_list.html', context)


def person_form(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        print(form)
    context = {'form': form}
    return render(request, 'person_form.html', context)


def form_form(request):
    form = PrForm()
    if request.method == 'POST':
        form = PrForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    context = {'form': form}
    return render(request, 'form_django.html', context)


class HomeworkCreate(CreateView):
    form_class = HomeworkForm
    model = HomeWork
    template_name = 'home_form.html'
    success_url = 'http://127.0.0.1:8000/homework'


def login(request):
    form = MyUserForm()
    print(request.COOKIES)
    print(request.COOKIES.get('name'))
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    context = {'form': form}
    response = render(request, 'login.html', context)
    response.set_cookie('color', request.COOKIES.get('color'))
    return response


"""КОРЗИНА"""


def get_products(request):
    product = Product.objects.all()
    category = Category.objects.all()
    context = {'categories': category, 'product': product}
    return render(request, 'products.html', context)


def get_categories(request, pk):
    category = Category.objects.filter(id=pk)
    product = Product.objects.filter(category_id=pk)
    context = {'categories': category, 'product': product}
    return render(request, 'products.html', context)
