from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tastecuba (request) :
    return render(request,'TASTECUBAPP/tastecuba.html')
def people (request) :
    return render(request,'TASTECUBAPP/people.html')
def origins (request) :
    return render(request,'TASTECUBAPP/origins.html')
def nature (request) :
    return render(request,'TASTECUBAPP/nature.html')
def join (request) :
    return render(request,'TASTECUBAPP/join.html')
def create_account (request) :
    return render(request,'TASTECUBAPP/create_account.html')

