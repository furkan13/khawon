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

user=get_user_model()






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


def reviews(request):
 return render(request, 'home/reviews.html')
def discounts(request):
 return render(request, 'home/discounts.html')
def signup(request):
 if request.method == "POST":
  print(request.POST)

  username = request.POST.get('username')
  password = request.POST.get('password')
  email = request.POST.get('email')
  user.username = username
  user.password = password
  user.email = email

  try:
   ret = user.objects.create(username=username, password=password, email=email)
  except Exception as e:
   
   return render(request, "home/home.html")
  if ret:
   return render(request, "home/login.html")

 return render(request, "home/signup.html")


