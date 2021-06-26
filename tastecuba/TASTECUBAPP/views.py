from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

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
def loggedin (request):
    return render(request, 'TASTECUBAPP/loggedin.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("TASTECUBAPP/templates/TASTECUBAPP")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render (request=request, template_name="TASTECUBAPP/register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/loggedin")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="TASTECUBAPP/login.html", context={"login_form":form})