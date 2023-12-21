from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.http import HttpResponseRedirect
from currency_converter.models import EventInsert


def indexpage(request):
    if request.user.is_authenticated == False:
        return  redirect('login')
    template = 'index.html'
    return render(request, template)

def register_request(request):
    if request.user.is_authenticated:
        return  redirect('indexpage')
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('indexpage')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.user.is_authenticated:
        return  redirect('indexpage')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('indexpage')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)


def insertRecord(request):
    if request.method=='POST':
            saveRecord = EventInsert()
            saveRecord.from_currency = request.POST.get('from_currency')
            saveRecord.target_currency = request.POST.get('target_currency')
            saveRecord.from_price = request.POST.get('from_price')
            saveRecord.target_price = request.POST.get('target_price')
            saveRecord.save()
            messages.success(request,' Record Added successfully')
            return render(request, "formTry.html",{})
    else:
        return render(request, "formTry.html",{})
