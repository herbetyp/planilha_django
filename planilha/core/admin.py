from django.contrib import admin

from planilha.core import models


@admin.register(models.Spent)
class SpentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'spent', 'date', 'value', 'created_at', 'updated_at')
    list_filter = ('date',)
    search_fields = ('spent',)


@admin.register(models.Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'income',
        'save_percent',
        'month',
        'year',
        'created_at',
        'updated_at',
    )
