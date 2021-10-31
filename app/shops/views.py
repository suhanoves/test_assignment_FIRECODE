from django.db.models import Q
from django.utils import timezone
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
    """API endpoint that allows streets of city to be viewed."""

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
    """API endpoint that allows shops to be viewed or edited."""

    queryset = Shop.objects.all()
    serializer_class = ShopCreateSerializer
    filterset_fields = ['city', 'city__name', 'street', 'street__name']

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve',):
            return ShopDetailSerializer
        return super().get_serializer_class()  # for create/destroy/update

    def get_queryset(self):

        queryset = super().get_queryset()

        is_open = self.request.query_params.get('open')
        current_time = timezone.localtime(timezone.now()).time()

        if is_open == '1':
            queryset = queryset.filter(
                opening_time__lte=current_time,
                closing_time__gte=current_time
            )
        elif is_open == '0':
            queryset = queryset.filter(
                Q(opening_time__gt=current_time)
                | Q(closing_time__lt=current_time)
            )

        return queryset
