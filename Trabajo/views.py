from django.http import HttpResponse
from django.shortcuts import render
from .forms import TrabajoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse("Inicio")

@login_required(login_url='/cuenta/login/')
def new(request):
    title = "Trabajo"
    if request.method == 'POST':
        form = TrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TrabajoForm()
            return render(request,'trabajo/new.html',{'form':form,'title':title})
        else:
            return render(request,'trabajo/new.html',{'form':form,'title':title})
    if request.method == 'GET':
        form = TrabajoForm()
        return render(request,'trabajo/new.html',{'form':form,'title':title})