from django import *

from deporte.models import Deporte

class FormularioDeporte(forms.ModelForm):
	class Meta:
		model = Deporte
		fields = ["nombre","descripcion"]