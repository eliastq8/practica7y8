from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .serializer import FrutaSerializer, QuesoSerializer
from .models import Fruta, Queso
from rest_framework import viewsets
from .form import Fruta
from django.contrib.auth.decorators import login_required
# Create your views here.

    
class QuesoViewsets(viewsets.ModelViewSet):
    queryset=Queso.objects.all()
    serializer_class=QuesoSerializer
    
def holamundo(request):
    return HttpResponse("Hola mundo")

def home(request):
    return render(request, "home.html")

def registro(request):
    if request.method =='GET':
        return render(request, "registro.html",{
            "form":UserCreationForm
        })
    else:
        req=request.POST
        if req['password1']==req['password2']:
            try:
                user=User.objects.create_user(
                    username=req['username'],
                    password=req['password1']
                )
                user.save()
                login(request,user)
                return redirect('/')
            except IntegrityError as ie:
                return render(request, "registro.html",{
                "form":UserCreationForm,
                "msg":"Usuario ya existente, usar otro nombre de usuario"
            })
            except Exception as e:
                return render(request, "registro.html",{
                "form":UserCreationForm,
                "msg":f"Error: {e}"
            })
        else:
            return render(request, "registro.html",{
                "form":UserCreationForm,
                "msg":"Favor de verificar que las contraseñas sean correctas"
        })


def IniciarSesion(request):
    if request.method == "GET":
        return render(request,"login.html",{
            "form":AuthenticationForm,
            
        })
    else:
        try:
            user=authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return render(request,"login.html",{
                "form":AuthenticationForm,
                "msg":"El usuario o la contraseña son incorrectos"
            })
        
        except Exception as e:
                return render(request,"login.html",{
                "form":AuthenticationForm,
                "msg":f"Error: {e}"
            })
    
def cerrarsesion(request):
    logout(request)
    return redirect('/')

@login_required
def frutas(request):
    if request.method == "GET":
        return render(request, "frutas.html",{
        "form":Fruta  
        })
    else:
        try:
            form=Fruta(request.POST)
            if form.is_valid():
                nuevo=form.save(commit=False)
                if request.user.is_authenticated:
                    nuevo.usuario=request.user
                    nuevo.save()
                    return redirect('/')
                else:
                    return render(request, "frutas.html",{
                    "form":Fruta,
                    "msg":"Este formulario no es valido"
                    }) 
            else:
                return render(request, "frutas.html",{
                    "form":Fruta,
                    "msg":"Este formulario no es valido"
                })
        except Exception as e:
                return render(request, "frutas.html",{
                    "form":Fruta,
                "msg":f"Error: {e}"
            })