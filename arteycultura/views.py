from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import *
from django.template.loader import *

from django.contrib.auth import *
from django.contrib.auth.forms import *

def inicio(request):
	return  render(request,"inicio.html")

def enviarCorreo(request):
	#correo = EmailMessage("Prueba de correo", "Saludos",to=["maxxharry@live.com.mx"])
	#correo.send()
	diccionario = {"x":"","nombre":"Jairo"}
	plantilla = get_template("correo.html")
	body = plantilla.render(diccionario)
	correo = EmailMultiAlternatives("Prueba2","Mensaje de Purbea","mickrig2200@gmail.com",["maxxharry@live.com.mx"],["maxxharry@live.com.mx"])
	correo.attach_alternative(body,"text/html")
	correo.send()
	return HttpResponse("Hola")

def ingresar(request):
	f = AuthenticationForm()
	if request.method == "POST":
		f= AuthenticationForm(data = request.POST)
		if f.is_valid():
			u = request.POST["username"]
			p = request.POST["password"]
			usr = authenticate(username = u, password = p)
			if usr is not None:
				login(request,usr)
				request.session["variableSesion"] = u

	return render(request,"Login.html",{"formulario":f})

def registrarUsuario(request):
	f = UserCreationForm()
	if request.method == "POST":
		f = UserCreationForm(data = request.POST)
		if f.is_valid():
			usr = f.save()

	f.fields["username"].help_text = None
	f.fields["password1"].help_text = None
	f.fields["password2"].help_text = None
	return render(request,"agregarusuario.html",{"formulario":f})

def salir (request):
	logout(request)
	return HttpResponse("Fuera!")