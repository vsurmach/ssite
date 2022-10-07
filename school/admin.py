from django.contrib import admin

from school.models import SchoolPerson, University, LevakModel

admin.site.register(University)
admin.site.register(LevakModel)


@admin.register(SchoolPerson)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'show_average')
    # fields = ('name', 'age', 'email')
    # list_display_links = ('name', 'age', 'email')
    # search_fields = ('name', )


    def show_average(self, obj):
        from django.db.models import Avg
        # result = SchoolPerson.objects.filter(name=obj).aggregate(Avg("age"))
        # return result["age__avg"]
        levak = LevakModel.objects.get(pk=1)
        return levak.book
