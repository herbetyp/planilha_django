from django.contrib import admin

from planilha.core import models


@admin.register(models.Spent)
class SpentAdmin(admin.ModelAdmin):
    list_display = ('id', 'spent', 'date', 'value')
    list_filter = ('date',)
    search_fields = ('spent',)
