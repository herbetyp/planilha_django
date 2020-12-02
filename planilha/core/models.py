from datetime import date

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Criado', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado', auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)


class Spent(AbstractBaseModel):
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='spent'
    )
    spent = models.CharField(verbose_name='Gasto', max_length=50, null=True, blank=True)
    month = models.IntegerField(verbose_name='Mês', default=date.today().month)
    year = models.IntegerField(verbose_name='Ano', default=date.today().year)
    date = models.DateField(verbose_name='Data', null=True, blank=True)
    value = models.DecimalField(
        'Valor', max_digits=15, decimal_places=2, null=True, blank=True
    )

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ('-id',)

    def __str__(self):
        return self.spent


class Income(AbstractBaseModel):
    user = models.ForeignKey(
        'auth.User', on_delete=models.DO_NOTHING, related_name='income'
    )
    income = models.DecimalField(
        verbose_name='Renda Bruta Mensal',
        max_digits=15,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
    )
    month = models.IntegerField(verbose_name='Mês', default=date.today().month)
    year = models.IntegerField(verbose_name='Ano', default=date.today().year)
    save_percent = models.IntegerField(
        verbose_name='Pocentagem Ah Economizar',
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
    )

    class Meta:
        verbose_name = 'Renda Mensal Bruta'
        verbose_name_plural = 'Rendas Mensais Brutas'
        ordering = ('-id',)

    def __str__(self):
        return str(self.income)
