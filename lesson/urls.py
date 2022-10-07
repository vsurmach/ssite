from django.urls import path

from .views import get_car, get_phone, get_fk_car, add_person, person_list, person_form, form_form, HomeworkCreate, \
    login, get_products, get_categories

app_name = "lesson"

urlpatterns = [
    path('get_car/', get_car, name='get_car'),
    path('get_phone/', get_phone, name='get_phone'),
    path('fk_get/', get_fk_car, name='get_fk_car'),
    # path('login_1', login_1, name='login_1'),
    path('add_person/', add_person, name='add_person'),
    path('get_person/', person_list, name='get_person'),
    path('person_form/', person_form, name='person_form'),
    path('form/', form_form, name='form_form'),
    path('homework/', HomeworkCreate.as_view()),
    path('login/', login, name='login'),
    path('products/', get_products, name='get_products'),
    path('categories/<int:pk>', get_categories, name='get_categories'),
]

