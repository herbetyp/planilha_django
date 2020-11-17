from django import forms
from django.contrib.auth.models import User

from planilha.core.models import Income


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Senha atual', widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='Nova senha', widget=forms.PasswordInput())
    new_password2 = forms.CharField(
        label='Repita a nova senha', widget=forms.PasswordInput(),
    )

    class Meta:
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')

        if len(password1) < 6 or len(password2) < 6:
            self.add_error('new_password2', 'Senha deve conter 6 ou mais carácteres!')

        if not self.user.check_password(old_password):
            self.add_error('old_password', 'Senha incorreta!')

        if password1 != password2:
            self.add_error('new_password2', 'Senhas não conferem!')

    def save(self):
        new_password = self.cleaned_data.get('new_password2')
        self.user.set_password(new_password)
        self.user.save()

        return self.user


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(
        label='Senha',
        help_text='senha precisa ter 6 ou mais carácteres.',
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(label='Repetir Senha', widget=forms.PasswordInput())

    class Meta:
        fields = '__all__'

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if User.objects.filter(username=username).exists():
            return self.add_error('username', 'usuário já existe.')

        if User.objects.filter(email=email).exists():
            return self.add_error('email', 'email já existe.')

        if len(password) < 6 or len(password2) < 6:
            return self.add_error('password', 'senha precisa ter 6 ou mais carácteres.')

        if password != password2:
            return self.add_error('password2', 'senhas não conferem')

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()

        Income.objects.create(user=user)
