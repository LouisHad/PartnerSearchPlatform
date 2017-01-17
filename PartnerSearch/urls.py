from django.conf.urls import url
from PartnerSearch import views

urlpatterns =[
    url(r'register$',views.register, name='register'),
    url(r'profile$', views.profile, name='profile'),
    url(r'addinstitution$', views.add_institution, name='institution'),
    url(r'exchangeform$', views.exchange, name='exchangeForm'),
    url(r'exchangeRequest$', views.exchangeRequest, name='exchangeRequest'),
    url(r'fundedform$', views.funded, name='fundedForm'),
    url(r'fundedRequest$', views.fundedRequest, name='fundedRequest'),

]