from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from planilha.core.forms import SpentForm, IncomeForm
from planilha.core.models import Spent, Income
from planilha.core import months


@login_required
def home_view(request):
    context = {}
    context['form'] = SpentForm()
    context['form_income'] = IncomeForm()
    context['months'] = months.MONTHS

    context['spents'] = (
        Spent.objects.filter(user=request.user)
        .values('pk', 'spent', 'date', 'value', 'created_at', 'updated_at')
        .order_by('-updated_at')[:10]
    )

    return render(request, 'core/home.html', context)


@login_required
def income_view(request, month, year=date.today().year):
    month_number = months.MONTHS.get(month)
    income, _ = Income.objects.get_or_create(
        user=request.user, month=month_number, year=year
    )
    if request.method == 'POST':
        form = IncomeForm(data=request.POST, instance=income)

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
    Spent.objects.get(pk=pk).delete()

    messages.success(request, 'Conta DELETADA com sucesso.')
    return JsonResponse({'url': reverse_lazy('core:month', args=[month])}, status=200)


@login_required
def update_spent_view(request, pk, month, year):
    spent = Spent.objects.get(user=request.user, pk=pk)
    month_number = months.MONTHS.get(month)

    if request.method == 'POST':
        form = SpentForm(
            data=request.POST,
            instance=spent,
            month=month_number,
            year=year,
        )
        form = SpentForm(
            data=request.POST,
            instance=spent,
            month=month_number,
            year=year,
        )
        if form.is_valid():
            form.save()

            messages.success(
                request, f'Conta <strong>{form.instance}</strong> ALTERADA com sucesso.'
            )
            return JsonResponse(
                {'url': reverse_lazy('core:month', args=[month])}, status=200
            )

        return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'spent': spent.spent, 'date': spent.date, 'value': spent.value})


@login_required
def create_spent_view(request, month, year):
    if request.method == 'POST':
        month_number = months.MONTHS.get(month)
        form = SpentForm(
            data=request.POST,
            instance=Spent(user=request.user),
            month=month_number,
            year=year,
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
    form_income = IncomeForm()
    month_number = months.MONTHS.get(month)
    month_name = ''.join([k for k, v in months.MONTHS.items() if v == month_number])
    year = int(request.GET.get('year')) if request.GET.get('year') else date.today().year

    context['form'] = SpentForm()
    context['month_name'] = month_name
    context['form_income'] = form_income
    context['year'] = year
    context['fixeds_accounts'] = Spent.objects.filter(
        user=request.user, fixed_account=True
    ).values('pk', 'spent', 'date', 'value')

    context['spents'] = Spent.objects.filter(
        user=request.user, month=month_number, year=year, fixed_account=False
    ).values('pk', 'spent', 'date', 'value')

    income = (
        Income.objects.filter(user=request.user, month=month_number, year=year)
        .values('income', 'save_percent')
        .last()
    )

    if income:
        context['income'] = income
        context['percent'] = income['income'] * income['save_percent'] / 100
        if context['spents']:
            context['total_spents'] = (
                Spent.objects.filter(
                    user=request.user,
                    month=month_number,
                    year=year,
                )
                .aggregate(Sum('value'))
                .get('value__sum')
            )
            context['balance'] = (
                income['income'] - context['total_spents'] - context['percent']
            )

    return render(request, 'core/month.html', context)
