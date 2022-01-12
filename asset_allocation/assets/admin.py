from django.contrib import admin


from assets import models


class CurrencyAdmin(admin.ModelAdmin):
    """Представление валюты в админке"""
    list_display = ('id', 'name', 'iso_code', 'symbol')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'iso_code')


class StockExchangeAdmin(admin.ModelAdmin):
    """Представление биржи в админке"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CountryGroupAdmin(admin.ModelAdmin):
    """Представление группы стран в админке"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(models.Currency, CurrencyAdmin)
admin.site.register(models.StockExchange, StockExchangeAdmin)
admin.site.register(models.CountryGroup, CountryGroupAdmin)

admin.site.site_header = 'Размещение активов'
admin.site.site_title = 'Размещение активов'
