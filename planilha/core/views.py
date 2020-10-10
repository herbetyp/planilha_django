from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render

from planilha.core import forms
from planilha.core import models


def home_view(request):
    form = forms.SpentForm()
    spents = models.Spent.objects.all()

    return render(request, 'core/home.html', {'spents': spents, 'form': form})


def delete_spent_view(request, pk):
    models.Spent.objects.get(pk=pk).delete()

    messages.add_message(request, messages.SUCCESS, 'Gasto DELETADO com sucesso.')
    return redirect('core:home')


def update_spent_view(request, pk):
    spent = models.Spent.objects.get(user=request.user, pk=pk)

    if request.method == 'POST':
        form = forms.SpentForm(data=request.POST, instance=spent)
        if form.is_valid():
            form.save()

            messages.add_message(
                request, messages.SUCCESS, 'Gasto ALTERADO com sucesso.'
            )
            return redirect('core:home')

    return JsonResponse(
        {'spent': spent.spent, 'date': spent.date, 'value': spent.value}
    )


def create_spent_view(request):
    if request.method == 'POST':
        form = forms.SpentForm(
            data=request.POST, instance=models.Spent(user=request.user)
        )
        if form.is_valid():
            form.save()

            messages.add_message(
                request, messages.SUCCESS, 'Gasto ADICIONADO com sucesso.'
            )
            return redirect('core:home')
