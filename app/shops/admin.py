from django.contrib import admin

from shops.models import City, Street, Shop


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'city',)
    list_select_related = ('city',)
    list_filter = ('city',)
    search_fields = ('name', 'city__name',)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'city', 'street', 'building', 'opening_time', 'closing_time',
    )
    list_select_related = ('city', 'street',)
    list_filter = ('city',)
    search_fields = ('name', 'city__name', 'street__name',)
