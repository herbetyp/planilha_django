from django import forms

from planilha.core import models


class SpentForm(forms.ModelForm):
    spent = forms.CharField(label='Gasto')
    date = forms.DateField(label='Data')
    value = forms.FloatField(min_value=1.0)

    class Meta:
        model = models.Spent
        fields = ['spent', 'date', 'value']
