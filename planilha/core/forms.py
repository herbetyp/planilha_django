from django import forms

from planilha.core import models


class SpentForm(forms.ModelForm):
    spent = forms.CharField(label='Gasto')
    date = forms.DateField(label='Data')
    value = forms.FloatField(min_value=1.0)

    class Meta:
        model = models.Spent
        fields = ['spent', 'date', 'value']


class IncomeForm(forms.ModelForm):
    income = forms.CharField(
        label='Renda',
        initial='0.00',
        widget=forms.TextInput(attrs={'type': 'tel', 'class': 'form-control'}),
    )
    save_percent = forms.CharField(
        label='Guardar em %',
        initial='0.00',
        widget=forms.TextInput(attrs={'type': 'tel', 'class': 'form-control'}),
    )

    class Meta:
        model = models.Income
        fields = ['income', 'save_percent']
