from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserManager(auth_models.BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("La dirección de Correo Electrónico no puede estar vacía.")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_superuser = user.is_staff = True
        user.save(using=self._db)
        return user

@python_2_unicode_compatible
class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(_('E-mail'), unique=True)
    first_name = models.CharField(_('Nombre(s)'), max_length=50, blank=True)
    last_name = models.CharField(_('Apellidos'), max_length=50, blank=True)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_active = models.BooleanField(_('Es Activo'), default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        if self.first_name == '' and self.last_name == '':
            return '{0}'.format(self.email)
        return '{0} {1}'.format(self.get_full_name(), self.email)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
