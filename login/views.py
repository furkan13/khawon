from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.urls import reverse
from django.template.context_processors import csrf
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,


)
from.models import customer

from  django.db.models import Q










# Create your views here.













