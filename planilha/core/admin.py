from django.contrib import admin

from planilha.core import models


@admin.register(models.Spent)
class SpentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'spent', 'value', 'created_at', 'updated_at')
    search_fields = ('spent',)


@admin.register(models.Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'income',
        'save_percent',
        'created_at',
        'updated_at',
    )
