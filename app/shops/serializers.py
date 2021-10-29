from rest_framework import serializers

from shops.models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name',)


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('id', 'name', 'city',)


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    street = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Shop
        fields = (
            'id', 'name', 'city', 'street', 'building',
            'opening_time', 'closing_time', 'is_open',
        )
