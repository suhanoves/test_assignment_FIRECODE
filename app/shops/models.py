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
