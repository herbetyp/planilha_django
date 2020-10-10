from django import forms

from planilha.core import models


class SpentForm(forms.ModelForm):
    spent = forms.CharField(label='Gasto')
    date = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))
    value = forms.NumberInput()

    class Meta:
        model = models.Spent
        fields = ['spent', 'date', 'value']
