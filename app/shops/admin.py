from django.contrib import admin

from shops.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
