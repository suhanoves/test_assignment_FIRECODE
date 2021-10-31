from rest_framework import generics, viewsets, serializers

from shops.models import City, Street, Shop
from shops.serializers import CitySerializer, StreetSerializer, \
    ShopCreateSerializer, ShopDetailSerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows cities to be viewed or edited."""
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer


class StreetViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows streets to be viewed or edited."""
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class StreetOfCityView(generics.ListAPIView):
    """API endpoint that allows streets of city to be viewed"""
    serializer_class = StreetSerializer

    def get_queryset(self):
        """
        Return a list of all the streets for the city
        as determined by the city_id of the URL.
        """
        city_id = self.kwargs['city_id']

        if not City.objects.filter(id=city_id).exists():
            raise serializers.ValidationError(
                {"error": "города с таким id не существует"}
            )

        return Street.objects.filter(city_id=city_id).order_by('name')


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
