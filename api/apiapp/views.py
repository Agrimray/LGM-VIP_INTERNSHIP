from urllib import response
from django.shortcuts import render
from django.core import files
from django.http.response import HttpResponse, HttpResponseBase
from django.shortcuts import render,redirect
import requests
# Create your views here.
def allEmployee(request):
    return render(request,'showEmployee.html')
    #return redirect('/apiapp/showEmp')
    #return HttpResponse("HE")

def home(request):
    response=requests.get('https://reqres.in/api/users?page=1').json()
    return render(request,'showEmployee.html',{'response':response})
    
    #
