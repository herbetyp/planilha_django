from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


class Spent(models.Model):
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='spent'
    )
    spent = models.CharField(verbose_name='Gasto', max_length=50, null=True, blank=True)
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


class Income(models.Model):
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, related_name='income'
    )
    income = models.DecimalField(
        verbose_name='Renda Bruta Mensal', max_digits=15, decimal_places=2
    )
    save_percent = models.IntegerField(
        verbose_name='Pocentagem Ah Economizar',
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
    )

    class Meta:
        verbose_name = 'Renda Mensal Bruta'
        verbose_name_plural = 'Rendas Mensais Brutas'
        ordering = ('-id',)

    def __str__(self):
        return str(self.income)
