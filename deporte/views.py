from django.shortcuts import *
from django.http import HttpResponse
from deporte.formulario import FormularioDeporte
from django.views import generic
from .models import Deporte

# Create your views here.
def inicio(request):
	#return HttpResponse("<a href='deporte/add'>Agregar</a>")
	return render(request, "deporte.html")

def agregardeporte(request):
	formulario = FormularioDeporte()
	if request.method == "POST":
		formulario= FormularioDeporte(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect("/")
	return  render(request,"deporte.html",{"form":formulario})

class ListaActividades(generic.ListView):
	model = Deporte
	context_object_name = "actividadesdeportes"
	template_name  = "deporte.html"