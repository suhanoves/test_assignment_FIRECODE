from rest_framework import viewsets

from shops.models import City, Street, Shop
from shops.serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer


class StreetViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows streets to be viewed or edited.
    """
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class ShopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shops to be viewed or edited.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
