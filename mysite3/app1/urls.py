from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #path('add/', views.AirportCreateView.as_view(), name='airport_add'),
    #url(r'^details/', views.details, name='details'),
    url(r'^details/', views.index, name='index'),
    url(r'^forms/', views.forms, name='forms'),
    url(r'^finalpage/', views.finalpage, name='finalpage')
    ]
