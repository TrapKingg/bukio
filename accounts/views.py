from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.debug import sensitive_variables
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

from accounts.forms import UserRegistrationForm
from core.models import User
from accounts.models import Profile
# Create your views here.
def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Ya existe un usuario registrado con el mismo e-mail'
    return JsonResponse(data)

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #Creamos un nuevo objeto usuario
            new_user = user_form.save(commit=False)
            #Insertamos la contraseña
            new_user.set_password(user_form.cleaned_data['password'])
            #Guardamos el objeto usuario
            new_user.save()
            messages.success(request, '¡Registro Éxitoso!')
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
        else:
            messages.warning(request, _('Hubo un error al registrarse, por favor intente nuevamente.'))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})
