from django.conf.urls import url
from PartnerSearch import views

urlpatterns =[
    url(r'register$',views.register, name='register'),
    url(r'profile$', views.profile, name='profile'),
    url(r'exchangeForm$', views.exchange, name='exchange'),
    url(r'exchangeForm$', views.institution, name='institution'),
    url(r'exchangeForm$', views.funded, name='funded'),
]