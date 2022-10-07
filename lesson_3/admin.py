from django.contrib import admin

from .models import CustomUser, FaceBook

admin.site.register(FaceBook)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)


# admin.site.register(CustomUser)