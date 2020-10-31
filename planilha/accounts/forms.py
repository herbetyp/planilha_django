from django import forms


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
