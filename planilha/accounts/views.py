from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render


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

        return redirect('accounts:login')

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    auth.logout(request)

    messages.info(request, 'Você foi deslogado.')
    return redirect('accounts:login')
