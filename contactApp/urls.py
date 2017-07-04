from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.contact_form, name='contactForm'),
    url(r'^contact/$', views.contact_submit, name='contactSubmit'),
]