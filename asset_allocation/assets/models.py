from django.db import models


class Currency(models.Model):
    """Валюта"""
    name = models.CharField(max_length=20, verbose_name='Наименование')
    iso_code = models.CharField(max_length=3, verbose_name='Код ISO 4217')
    symbol = models.CharField(max_length=1, verbose_name='Символ')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'currency'
        ordering = ('name',)
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
