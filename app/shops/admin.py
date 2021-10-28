from django.contrib import admin

from shops.models import City, Street


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'city',)
    list_select_related = ('city',)
    list_filter = ('city',)
    search_fields = ('name', 'city__name',)
