from datetime import time

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase, TransactionTestCase

from shops.models import City, Street, Shop


class CityTest(TestCase):
    def setUp(self):
        City.objects.create(
            name='Москва'
        )

    def test_city_retrieve(self):
        moscow = City.objects.get(name="Москва")
        self.assertEqual(str(moscow), 'Москва')


class StreetTest(TransactionTestCase):
    def setUp(self):
        moscow = City.objects.create(name='Москва')
        Street.objects.create(name='Пушкинская', city=moscow)

        self.street = Street.objects.get(name="Пушкинская")
        self.city = City.objects.get(name="Москва")

    def test_street_retrieve(self):
        self.assertEqual(self.street.name, 'Пушкинская')
        self.assertEqual(str(self.street), 'Пушкинская (Москва)')
        self.assertEqual(self.street.city, self.city)

    def test_street_duplicate_error(self):
        with self.assertRaises(IntegrityError):
            Street.objects.create(name='Пушкинская', city=self.city)


class ShopTest(TransactionTestCase):
    def setUp(self):
        moscow = City.objects.create(name='Москва')
        moscow_street = Street.objects.create(name='Пушкинская', city=moscow)

        Shop.objects.create(
            name='Московский магазин',
            city=moscow,
            street=moscow_street,
            building='1',
            opening_time=time(hour=10),
            closing_time=time(hour=22),
        )

        self.moscow = City.objects.get(name="Москва")
        self.moscow_street = Street.objects.get(city=moscow)
        self.moscow_shop = Shop.objects.get(city=moscow)

    def test_shop_retrieve(self):
        self.assertEqual(self.moscow_shop.name, 'Московский магазин')

    def test_shop_duplicate_error(self):
        with self.assertRaises(ValidationError) as e:
            Shop.objects.create(
                name='Московский магазин',
                city=self.moscow,
                street=self.moscow_street,
                building='1',
                opening_time=time(hour=6),
                closing_time=time(hour=18),
            )

        self.assertEqual(
            e.exception.message_dict,
            {'__all__': ['Магазин с такими значениями полей Название магазина,'
                         ' Город, Улица и Номер дома уже существует.']}
        )

    def test_shop_with_street_from_another_city(self):
        rostov = City.objects.create(name='Ростов')
        rostov_street = Street.objects.create(name='Пушкинская', city=rostov)

        with self.assertRaises(ValidationError) as e:
            Shop.objects.create(
                name='Ошибочный',
                city=self.moscow,
                street=rostov_street,
                building='1',
                opening_time=time(hour=10),
                closing_time=time(hour=22),
            )

        self.assertEqual(
            e.exception.message_dict,
            {'city': ['указанная улица не принадлежит указанному городу']}
        )

    def test_shop_with_wrong_working_hours(self):
        with self.assertRaises(IntegrityError):
            Shop.objects.create(
                name='Неправильный',
                city=self.moscow,
                street=self.moscow_street,
                building='1',
                opening_time=time(hour=22),
                closing_time=time(hour=10),
            )
