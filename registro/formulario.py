from django import *

from registro.models import Persona

class FormularioPersona(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ["nombre","correo","sexo"]
	