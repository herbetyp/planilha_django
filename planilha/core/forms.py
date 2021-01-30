from django import forms

from planilha.core import models


class SpentForm(forms.ModelForm):
    spent = forms.CharField(label='Conta')
    value = forms.DecimalField(label='Valor', min_value=1.0)

    class Meta:
        model = models.Spent
        fields = [
            'spent',
            'value',
            'month',
            'year',
            'fixed_account',
            'parceled_out',
            'number_plots',
        ]

    def __init__(self, *args, **kwargs):
        self.month = kwargs.pop('month', None)
        self.year = kwargs.pop('year', None)
        super(SpentForm, self).__init__(*args, **kwargs)

        self.fields['month'].required = False
        self.fields['year'].required = False

    def clean(self):
        new_spent = self.cleaned_data.get('spent')
        new_value = self.cleaned_data.get('value')
        new_number_plots = self.cleaned_data.get('number_plots')

        qs = models.Spent.objects.filter(
            spent=new_spent, value=new_value, number_plots=new_number_plots
        )
        if qs.exists():
            raise forms.ValidationError('Conta já existe')

    def save(self):
        self.instance.month = self.month
        self.instance.year = self.year
        self.instance.save()


class IncomeForm(forms.ModelForm):
    income = forms.CharField(
        label='Renda de ',
        widget=forms.TextInput(attrs={'type': 'tel'}),
    )
    save_percent = forms.CharField(
        label='Guardar em %',
        widget=forms.TextInput(attrs={'type': 'tel'}),
    )
    year = forms.CharField(
        label='Definir ano',
        required=False,
        widget=forms.TextInput(attrs={'type': 'tel'}),
    )

    class Meta:
        model = models.Income
        fields = ['income', 'save_percent', 'year']
