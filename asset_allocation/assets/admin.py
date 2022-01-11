from django.contrib import admin


from assets import models


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'iso_code', 'symbol')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'iso_code')


admin.site.register(models.Currency, CurrencyAdmin)
