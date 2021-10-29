from django.db import models
from django.utils import timezone


class City(models.Model):
    name = models.CharField(
        verbose_name='название города',
        max_length=50,
        unique=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(
        verbose_name='название улицы',
        max_length=100,
        db_index=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='город',
        related_name='streets',
        related_query_name='street',
    )

    class Meta:
        verbose_name = 'улица'
        verbose_name_plural = 'улицы'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'city'),
                name='city_street_unique',
            )
        ]

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(
        verbose_name='название магазина',
        max_length=150,
        db_index=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='город',
        related_name='shops',
        related_query_name='shop',
    )
    street = models.ForeignKey(
        Street,
        on_delete=models.CASCADE,
        verbose_name='улица',
        related_name='shops',
        related_query_name='shop',
    )
    building = models.CharField(
        verbose_name='номер дома',
        max_length=10,
    )
    opening_time = models.TimeField(
        verbose_name='время открытия'
    )
    closing_time = models.TimeField(
        verbose_name='время закрытия'
    )

    @property
    def is_open(self):
        current_time = timezone.localtime(timezone.now()).time()
        return self.opening_time <= current_time <= self.closing_time

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'city', 'street', 'building'),
                name='shop_city_street_building_unique',
            ),
            models.CheckConstraint(
                check=models.Q(closing_time__gt=models.F('opening_time')),
                name='closing_time_gt_opening_time'
            )
        ]

    def __str__(self):
        return self.name
