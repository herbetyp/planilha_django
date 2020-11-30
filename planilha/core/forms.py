from django import forms

from planilha.core import models


class SpentForm(forms.ModelForm):
    spent = forms.CharField(label='Conta')
    date = forms.DateField(label='Data')
    value = forms.FloatField(label='Valor', min_value=1.0)
    month = forms.CharField(required=False, widget=forms.HiddenInput())
    year = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = models.Spent
        fields = ['spent', 'date', 'value', 'month', 'year']

    def __init__(self, *args, **kwargs):
        self.month = kwargs.pop('month', None)
        self.year = kwargs.pop('year', None)
        super(SpentForm, self).__init__(*args, **kwargs)

    def clean(self):
        new_spent = self.cleaned_data.get('spent')
        new_date = self.cleaned_data.get('date')
        new_value = self.cleaned_data.get('value')

        qs = models.Spent.objects.filter(
            spent=new_spent, date=new_date, value=new_value
        )
        if qs.exists():
            raise forms.ValidationError('Conta já existe')

    def save(self):
        self.instance.month = self.month
        self.instance.year = self.year
        self.instance.save()


class IncomeForm(forms.ModelForm):
    income = forms.CharField(
        label='Renda de ', widget=forms.TextInput(attrs={'type': 'tel'}),
    )
    save_percent = forms.CharField(
        label='Guardar em %', widget=forms.TextInput(attrs={'type': 'tel'}),
    )
    year = forms.CharField(
        label='Definir ano',
        required=False,
        help_text='Se não informado, considera o ano corrente.',
        widget=forms.TextInput(attrs={'type': 'tel'}),
    )

    class Meta:
        model = models.Income
        fields = ['income', 'save_percent', 'year']
