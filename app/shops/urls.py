from django.urls import include, path
from rest_framework import routers

from shops.views import CityViewSet, StreetViewSet, ShopViewSet, StreetOfCityView

router = routers.DefaultRouter()
router.register(r'city', CityViewSet)
router.register(r'street', StreetViewSet)
router.register(r'shop', ShopViewSet)

urlpatterns = [
    path('city/<int:city_id>/street/', StreetOfCityView.as_view()),
    path('', include(router.urls)),
]
