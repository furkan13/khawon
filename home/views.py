from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.urls import reverse
from django.template.context_processors import csrf
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,


)


from login.models import customer

user=customer






# Create your views here.
def home(request):
 return render(request,"home/home.html")


def log_in(request):
 context = {}

 if request.method == "POST":
  print(request.POST)

  username = request.POST.get('username')
  password = request.POST.get('password')

  user = authenticate(request, username=username, password=password)
  print(user)

  login(request,user)
  return HttpResponseRedirect(reverse('home'))
 else:
  return render(request,"home/login.html")





 return render(request, 'home/login.html')


def log_out(request):
  logout(request)

  return render(request,'home/home.html')




