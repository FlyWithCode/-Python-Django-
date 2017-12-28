from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requset):
     return HttpResponse("hello world !")

def home(req,number):
    print('home--test')
    number = str(number)
    print(number)
    return render(req,'index.html',{'number':number})