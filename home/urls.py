from django.conf.urls import url,include
from . import views
from  django.contrib.auth import (login)




urlpatterns = [

    url(r'^home/$', views.home,name='home'),
     url(r'^$', views.home),
    url(r'^log_in/$',views.log_in,name='login'),
url(r'^log_out/$',views.log_out,name='logout'),


]