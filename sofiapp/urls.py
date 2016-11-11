from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

app_name = 'sofiapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacto/$', views.contact, name='contact'),
    url(r'^proyectos/(?P<filter>.*)/$', views.projects, name='projects'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
