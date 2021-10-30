from rest_framework import viewsets

from shops.models import City, Street, Shop
from shops.serializers import CitySerializer, StreetSerializer, \
    ShopCreateSerializer, ShopDetailSerializer


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
    serializer_class = ShopCreateSerializer

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve',):
            return ShopDetailSerializer
        return super().get_serializer_class()  # for create/destroy/update
