from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UsuarioRegisterForm, UserForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    return HttpResponse("Inicio")

def register(request):
    title = 'Registrarse'
    if request.method == 'GET':
        form = UserForm()
        return render(request,'cuenta/register.html',{'form':form, 'title':title})

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'cuenta/register.html',{'form':form, 'title':title})
        else: 
            errors = form.errors
            messages.add_message(request,messages.ERROR, errors)
            return render(request,'cuenta/register.html',{'form':form,'title':title})

def login(request):
    title = 'Iniciar Sesion'
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request,'cuenta/login.html',{'form':form, 'title':title})

    if request.method == 'POST':
        form = UserLoginForm(request=request,data=request.POST)
        if form.is_valid():
            print("EXITO")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                #login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                #return render(request,'',{'form':form, 'title':title})
                return redirect('index')
            messages.success(request,"Inicio de sesion EXITOSO")
            return render(request,'cuenta/login.html',{'form':form, 'title':title})
        else: 
            print("FALLO")
            errors = form.errors
            print(errors)
            messages.add_message(request,messages.ERROR, errors)
            return render(request,'cuenta/login.html',{'form':form,'title':title})