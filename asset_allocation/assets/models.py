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


class StockExchange(models.Model):
    """Биржа"""
    name = models.CharField(max_length=20, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stock_exchange'
        ordering = ('name',)
        verbose_name = 'Биржа'
        verbose_name_plural = 'Биржи'


class CountryGroup(models.Model):
    """Группа стран"""
    name = models.CharField(max_length=25, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country_group'
        ordering = ('name',)
        verbose_name = 'Группа стран'
        verbose_name_plural = 'Группы стран'


class Country(models.Model):
    """Страна"""
    name = models.CharField(max_length=25, verbose_name='Наименование')
    flag = models.ImageField(upload_to='country_flags/', verbose_name='Флаг')
    country_group = models.ForeignKey(CountryGroup, on_delete=models.PROTECT, verbose_name='Группа стран')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'
        ordering = ('name',)
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
