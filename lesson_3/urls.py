from django.contrib import admin
from django.urls import path, include

from .views import login_view, login_success, validation_view

app_name = 'lesson_3'

urlpatterns = [
    path('my_login/', login_view, name='login_view'),
    path('login_success/', login_success, name='login_success'),
    path('validation/', validation_view, name='validation' )
]