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
