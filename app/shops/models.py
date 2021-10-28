from django.db import models


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
