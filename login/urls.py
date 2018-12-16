from django.conf.urls import url,include
from . import views




urlpatterns = [


url(r'^log_in/$', views.login),
    url(r'^$',views.login),


]