from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from shops.models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name',)


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('id', 'name', 'city',)
        validators = [
            UniqueTogetherValidator(
                queryset=Street.objects.all(),
                fields=('name', 'city',)
            ),
        ]


class ShopIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id',)


class ShopDetailSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    street = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Shop
        fields = (
            'id', 'name', 'city', 'street', 'building',
            'opening_time', 'closing_time',
        )


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            'id', 'name', 'city', 'street', 'building',
            'opening_time', 'closing_time',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Shop.objects.all(),
                fields=('name', 'city', 'street', 'building',)
            ),
        ]

    def validate(self, data):
        # Check that opening_time is before closing_time.
        if data['opening_time'] > data['closing_time']:
            raise ValidationError(
                'время закрытия магазина должно быть позже времени открытия'
            )
        # Checks that the street belongs to the city
        if data['street'].city != data['city']:
            raise ValidationError(
                'указанная улица не принадлежит указанному городу'
            )

        return data
