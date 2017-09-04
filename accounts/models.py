from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.

class Carrera(models.Model):
    carrera = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.carrera

class Semestre(models.Model):
    semestre = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.semestre

def upload_location(instance, filename):
    return 'profiles/%s/%s' %(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to=upload_location, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    carrera = models.ForeignKey(Carrera, verbose_name='Carrera', blank=True, null=True)
    semestre = models.ForeignKey(Semestre, verbose_name='Semestre', blank=True, null=True)

    def __str__(self):
        return '%s' % self.user.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
