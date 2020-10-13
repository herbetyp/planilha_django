from django.contrib import admin

from planilha.core import models


@admin.register(models.Spent)
class SpentAdmin(admin.ModelAdmin):
    list_display = ('id', 'spent', 'date', 'value')
    list_filter = ('date',)
    search_fields = ('spent',)


@admin.register(models.Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'income', 'save_percent')
