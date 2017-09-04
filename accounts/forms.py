from django import forms
from core.models import User
from django.utils.translation import ugettext as _
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_('Contraseña'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Repetir Contraseña'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(_('Las contraseñas no coinciden.'))
        return cd['password2']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'avatar', 'birth_date', 'carrera', 'semestre')
