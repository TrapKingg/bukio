from django.conf.urls import url
from accounts.views import register, validate_email
urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^ajax/validate_email/$', validate_email, name='validate_email'),
]
