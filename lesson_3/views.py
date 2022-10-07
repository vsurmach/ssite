from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import LoginForms, FormToValidate


def login_view(request):
    form = LoginForms()
    context = {'form': form}
    if request.user.is_authenticated:
        return redirect('lesson_3:login_success')

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lesson_3:login_success')
    return render(request, 'my_login.html', context)


def login_success(request):
    context = {'username': request.user.username}
    if request.method == 'POST':
        logout(request)
        return redirect('lesson_3:login_view')
    return render(request, 'main.html', context)


def validation_view(request):
    form = FormToValidate()
    if request.method == 'POST':
        form = FormToValidate(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            context = {'form': form}
            return render(request, 'validation.html', context)
    context = {'form': form}
    return render(request, 'validation.html', context)
