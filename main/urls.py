from django.urls import path

from .views import index, get_category

app_name = "main"

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:id>', get_category, name="get_category")
]