from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy

from planilha.core import forms
from planilha.core import models


def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        post = request.POST.copy()
        form = AuthenticationForm(data=post)

        if form.is_valid():
            auth.login(request, form.get_user())

            messages.success(request, 'Login realizado com sucesso.')
            return redirect('core:home')

        messages.error(
            request, 'Usuário não encontrado. Verifique se preencheu corretamente.'
        )
        return redirect('core:login')

    return render(request, 'core/login.html', {'form': form})


@login_required
def logout_view(request):
    auth.logout(request)

    messages.info(request, 'Você foi deslogado.')
    return redirect('core:login')


@login_required
def home_view(request):
    form = forms.SpentForm()

    return render(request, 'core/home.html', {'form': form})


@login_required
def income_view(request):
    if request.method == 'POST':
        income_value = request.POST.get('income')
        save_percent = request.POST.get('save_money')
        income = models.Income.objects.filter(user=request.user)

        if income.exists():
            income.update(income=income_value, save_percent=save_percent)
            messages.success(request, 'Dados ATUALIZADOS com sucesso.')
        else:
            income.create(
                user=request.user, income=income_value, save_percent=save_percent
            )
            messages.success(request, 'Dados SALVO com sucesso.')
        return redirect('core:home')


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
