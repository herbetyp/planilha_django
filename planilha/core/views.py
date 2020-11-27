import calendar
from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from planilha.core import forms
from planilha.core import models
from planilha.core import months


@login_required
def home_view(request):
    context = {}
    context['form'] = forms.SpentForm()
    context['form_income'] = forms.IncomeForm()
    context['months'] = months.MONTHS

    context['spents'] = (
        models.Spent.objects.filter(user=request.user)
        .values('pk', 'spent', 'date', 'value', 'created_at', 'updated_at')
        .order_by('-updated_at')[:10]
    )

    return render(request, 'core/home.html', context)


@login_required
def income_view(request, month, year=date.today().year):
    month_number = months.MONTHS.get(month)
    income, _ = models.Income.objects.get_or_create(
        user=request.user, month=month_number, year=year
    )
    if request.method == 'POST':
        form = forms.IncomeForm(data=request.POST, instance=income)

        if form.is_valid():
            form.save()

            messages.success(request, 'Dados SALVO com sucesso.')
            return JsonResponse(
                {'url': reverse_lazy('core:month', kwargs={'month': month})}, status=200
            )

        return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'income': income.income, 'save_percent': income.save_percent})


@login_required
def delete_spent_view(request, pk, month):
    models.Spent.objects.get(pk=pk).delete()

    messages.success(request, 'Conta DELETADA com sucesso.')
    return JsonResponse({'url': reverse_lazy('core:month', args=[month])}, status=200)


@login_required
def update_spent_view(request, pk, month):
    spent = models.Spent.objects.get(user=request.user, pk=pk)

    if request.method == 'POST':
        form = forms.SpentForm(data=request.POST, instance=spent)
        if form.is_valid():
            form.save()

            messages.success(
                request, f'Conta <strong>{form.instance}</strong> ALTERADA com sucesso.'
            )
            return JsonResponse(
                {'url': reverse_lazy('core:month', args=[month])}, status=200
            )

        return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse(
        {'spent': spent.spent, 'date': spent.date, 'value': spent.value}
    )


@login_required
def create_spent_view(request, month):
    if request.method == 'POST':
        form = forms.SpentForm(
            data=request.POST, instance=models.Spent(user=request.user)
        )
        if form.is_valid():
            form.save()

            messages.success(
                request,
                f'Conta <strong>{form.instance}</strong> ADICIONADA com sucesso.',
            )
            return JsonResponse(
                {'url': reverse_lazy('core:month', args=[month])}, status=200
            )

        return JsonResponse({'errors': form.errors}, status=400)


@login_required
def month_view(request, month):
    context = {}
    form_income = forms.IncomeForm()
    month_number = months.MONTHS.get(month)
    month_name = ''.join([k for k, v in months.MONTHS.items() if v == month_number])
    year = (
        int(request.GET.get('year')) if request.GET.get('year') else date.today().year
    )

    context['form'] = forms.SpentForm()
    context['month_name'] = month_name
    context['form_income'] = form_income
    context['year'] = year

    days = calendar.monthrange(year, month_number)
    context['spents'] = models.Spent.objects.filter(
        user=request.user,
        date__range=[f'{year}-{month_number}-01', f'{year}-{month_number}-{days[1]}'],
    ).values('pk', 'spent', 'date', 'value')

    income = (
        models.Income.objects.filter(user=request.user, month=month_number, year=year)
        .values('income', 'save_percent')
        .last()
    )

    if income:
        context['income'] = income
        context['percent'] = income['income'] * income['save_percent'] / 100
        if context['spents']:
            context['total_spents'] = (
                context['spents'].aggregate(Sum('value')).get('value__sum')
            )
            context['balance'] = (
                income['income'] - context['total_spents'] - context['percent']
            )

    return render(request, 'core/month.html', context)
