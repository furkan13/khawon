from django.conf.urls import url,include
from . import views
from .views import search
from  django.contrib.auth import (login)




urlpatterns = [

    url(r'^home/$', views.home,name='home'),

     url(r'^$', views.home),
    url(r'^log_in/$',views.log_in,name='login'),
     url(r'^log_out/$',views.log_out,name='logout'),
     url(r'^reviews/$',views.reviews,name='reviews'),
    url(r'^discounts/$', views.discounts, name='discounts'),

     url(r'^signup/$', views.signup, name='signup'),
    url(r'^search/$', views.search, name='search'),
    url(r'^bashmoti/$',views.bash,name='bash'),
    url(r'^skiplogin/$',views.slogin,name='skip'),



]