from django.contrib import admin
from django.utils.safestring import mark_safe


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


class ManagementCompanyAdmin(admin.ModelAdmin):
    """Представление управляющей компании в админке"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class BranchAdmin(admin.ModelAdmin):
    """Представление отрасли в админке"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CountryGroupAdmin(admin.ModelAdmin):
    """Представление группы стран в админке"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CountryAdmin(admin.ModelAdmin):
    """Представление страны в админке"""
    list_display = ('id', 'name', 'get_flag_image', 'country_group')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'country_group')

    def get_flag_image(self, obj: models.Country) -> str:
        return mark_safe(f'<img src="{obj.flag.url}" height="20" style="outline: 1px solid #bcbcbc">')

    get_flag_image.short_description = 'Флаг'


class AssetTypeAdmin(admin.ModelAdmin):
    """Представление типа актива в админке"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class AssetSubtypeAdmin(admin.ModelAdmin):
    """Представление подтипа актива в админке"""
    list_display = ('id', 'name', 'asset_type')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'asset_type')


admin.site.register(models.Currency, CurrencyAdmin)
admin.site.register(models.StockExchange, StockExchangeAdmin)
admin.site.register(models.ManagementCompany, ManagementCompanyAdmin)
admin.site.register(models.Branch, BranchAdmin)
admin.site.register(models.CountryGroup, CountryGroupAdmin)
admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.AssetType, AssetTypeAdmin)
admin.site.register(models.AssetSubtype, AssetSubtypeAdmin)

admin.site.site_header = 'Размещение активов'
admin.site.site_title = 'Размещение активов'
