from django.contrib import admin
from .models import Bmi

# Register your models here.


class BmiAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'height', 'bmi', 'trackDate')
    readonly_fields = ['bmi', 'trackDate']

admin.site.register(Bmi, BmiAdmin)