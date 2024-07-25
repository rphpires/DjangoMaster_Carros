from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)