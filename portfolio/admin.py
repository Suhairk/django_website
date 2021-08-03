from django.contrib import admin
from .models import projects , form
# Register your models here.

class projectsAdmin(admin.ModelAdmin):
    list_display =('name', 'des', 'image')


class formAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','message')



admin.site.register(projects,projectsAdmin)
admin.site.register(form,formAdmin)