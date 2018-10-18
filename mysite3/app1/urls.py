from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/', views.details, name='details'),
    url(r'^forms/', views.forms, name='forms'),
    url(r'^finalpage/', views.finalpage, name='finalpage')
    ]
