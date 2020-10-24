from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy

from planilha.core import forms
from planilha.core import models


@login_required
def home_view(request):
    form = forms.SpentForm()
    form_income = forms.IncomeForm()

    return render(request, 'core/home.html', {'form': form, 'form_income': form_income})


@login_required
def income_view(request):
    income, _ = models.Income.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = forms.IncomeForm(data=request.POST, instance=income)

        if form.is_valid():
            form.save()

            messages.success(request, 'Dados SALVO com sucesso.')
            return JsonResponse({'url': reverse_lazy('core:home')}, status=200)

        return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'income': income.income, 'save_percent': income.save_percent})


@login_required
def delete_spent_view(request, pk):
    models.Spent.objects.get(pk=pk).delete()

    messages.success(request, 'Gasto DELETADO com sucesso.')
    return redirect('core:home')


@login_required
def update_spent_view(request, pk):
    spent = models.Spent.objects.get(user=request.user, pk=pk)

    if request.method == 'POST':
        form = forms.SpentForm(data=request.POST, instance=spent)
        if form.is_valid():
            form.save()

            messages.success(request, 'Gasto ALTERADO com sucesso.')
            return JsonResponse({'url': reverse_lazy('core:home')}, status=200)

        return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse(
        {'spent': spent.spent, 'date': spent.date, 'value': spent.value}
    )


@login_required
def create_spent_view(request):
    if request.method == 'POST':
        form = forms.SpentForm(
            data=request.POST, instance=models.Spent(user=request.user)
        )
        if form.is_valid():
            form.save()

            messages.success(request, 'Gasto ADICIONADO com sucesso.')
            return JsonResponse({'url': reverse_lazy('core:home')}, status=200)

        return JsonResponse({'errors': form.errors}, status=400)
