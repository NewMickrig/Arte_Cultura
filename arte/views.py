from django.views import generic
from django.shortcuts import *
from django.http import HttpResponse
from arte.formulario import FormularioArte
from .models import Arte

# Create your views here.
def inicio(request):
	return render(request, "arte.html")
	#return HttpResponse("<a href='arte/add'>Agregar</a>")

def agregar(request):
	formulario = FormularioArte()
	if request.method == "POST":
		formulario= FormularioArte(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect("/")
	return  render(request,"arte.html",{"form":formulario})

class ListaActividades(generic.ListView):
	model = Arte
	context_object_name = "actividadesarte"
	template_name  = "arte.html"