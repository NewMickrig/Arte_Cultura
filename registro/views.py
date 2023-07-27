from django.shortcuts import *
from django.http import HttpResponse
from registro.formulario import FormularioPersona
from .models import Persona
from django.views import generic

# Create your views here.
def registro(request):
	formulario = FormularioPersona()
	if request.method == "POST":
		formulario= FormularioPersona(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect("/")
	return  render(request,"registro.html",{"form":formulario})

class ListaActividades(generic.ListView):
	model = Persona
	context_object_name = "Personas"
	template_name  = "registro.html"