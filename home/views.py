from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.db.models import  Q
from django.urls import reverse
from .models import restaurant
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from   khawoon.config import pagination


from django.template.context_processors import csrf
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,


)




user=get_user_model()






# Create your views here.
def home(request):

 lvl=2
 context={
  "lvl":lvl
 }
 return render(request,"home/home.html",context)


def log_in(request):
 context = {}

 if request.method == "POST":
  print(request.POST)

  username = request.POST.get('username')
  password = request.POST.get('password')


  user = authenticate(request, username=username, password=password)
  print(user)
  if user:
   login(request,user)
   return HttpResponseRedirect(reverse('bash'))
  else:
   return render(request, "home/LogIn.html")







 return render(request, 'home/LogIn.html')


def log_out(request):
  logout(request)

  return render(request,'home/home.html')


def reviews(request):
 return render(request, 'home/Restaurants.html')
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
   context={"error":'already used username'}


   return render(request, "home/SignUp.html",context)
  if ret:

      login(request,ret)
      return HttpResponseRedirect(reverse('home'))








 return render(request, "home/SignUp.html")






def search(request):
 template='home/search.html'
 query = request.GET.get('q')
 results = restaurant.objects.filter(Q(name__icontains=query)|Q(tag__icontains=query))
 pages=pagination(request,results,num=4)
 context={
     'iteams':pages[0],
     'page_range':pages[1],

 }




 return render(request,template,context)
def bash(request):
 return render(request,"home/bashmoti.html")
def slogin(request):
 if request.method == "POST":
  print(request.POST)

  username = request.POST.get('username')
  password = request.POST.get('password')


  user = authenticate(request, username=username, password=password)
  print(user)
  if user:
   login(request,user)
   return HttpResponseRedirect(reverse('home'))
  else:
   return render(request, "home/SkipLogIn.html")







 return render(request, 'home/SkipLogIn.html')


def sultan(request):
 return render(request,"home/sultanres.html")


def take(request):
 return render(request,"home/takeout.html")
def team(request):
 return render(request,"home/team.html")
def cherry(request):
 return render(request,"home/cherrryresturent.html")
def contact(request):
 return render(request,"home/contact.html")


def filter(request):
 return render(request,"home/searchd.html")









