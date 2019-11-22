from django.conf.urls import url,include
from . import views
from .views import search
from  django.contrib.auth import (login)




urlpatterns = [

    url(r'^home/$', views.home,name='home'),

     url(r'^$', views.home),
    url(r'^log_in/$',views.log_in,name='login'),
     url(r'^log_out/$',views.log_out,name='logout'),
     url(r'^restaurants/$',views.reviews,name='restaurant'),
    url(r'^discounts/$', views.discounts, name='discounts'),

     url(r'^signup/$', views.signup, name='signup'),
    url(r'^search/$', views.search, name='search'),
    url(r'^bashmoti/$',views.bash,name='bash'),
    url(r'^skiplogin/$',views.slogin,name='skip'),
    url(r'^sultan/$',views.sultan,name="sultan"),
    url(r'^takeout/$',views.take, name="take"),
url(r'^team/$',views.team, name="team"),
url(r'^cherry/$',views.cherry, name="cherry"),
url(r'^contact/$',views.contact, name="contact"),
url(r'^filter/$',views.filter, name="filter"),






]