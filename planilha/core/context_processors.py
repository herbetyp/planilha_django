from django.db.models import Sum

from planilha.core import models


def home_context(request):
    context = {}
    if request.user.is_authenticated:
        income = (
            models.Income.objects.filter(user=request.user)
            .values('income', 'save_percent')
            .last()
        )
        spents = models.Spent.objects.filter(user=request.user).values(
            'pk', 'spent', 'date', 'value'
        )

        context = {'income': income}
        context['percent'] = income['income'] * income['save_percent'] / 100
        if spents:
            context['spents'] = spents
            context['total_spents'] = spents.aggregate(Sum('value')).get('value__sum')
            context['balance'] = (
                income['income'] - context['total_spents'] - context['percent']
            )

    return context
