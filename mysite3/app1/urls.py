from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #path('add/', views.AirportCreateView.as_view(), name='airport_add'),
    #url(r'^payerdetails/', views.details, name='details'),
    url(r'^details/', views.index, name='index'),
    #url(r'^details_sub/', views.details, name='details'),
    url(r'^payerdetails/', views.payerdetails, name='payerdetails'),
    url(r'^details_sub/', views.details, name='details'),
    #url(r'^finalpage/', views.finalpage, name='finalpage'),
    url(r'^forms/', views.forms, name='forms')
    ]
