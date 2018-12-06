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
    url(r'^finalpage/', views.finalpage, name='finalpage'),
    url(r'^forms/', views.forms, name='forms'),
    url(r'^lastpage/', views.lastpage, name='lastpage'),
    url(r'^admin1/', views.admin ,name='admin'),
    url(r'^airport/', views.editAirport ,name='editA'),
    url(r'^aircraft/', views.editAircraft ,name='editAc'),
    #url(r'^demo/', views.demo ,name='demo')
    ]
