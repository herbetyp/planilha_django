from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from planilha.accounts import forms


@method_decorator(login_required, name='dispatch')
class CustomPasswordChangeView(auth_views.PasswordChangeView):
    form_class = forms.ChangePasswordForm
    template_name = 'accounts/change-password.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Senha Alterada com SUCESSO. Refaça o login!',
        )
        logout(self.request)
        return super().form_valid(form)


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
