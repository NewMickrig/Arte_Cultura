from django import *

from arte.models import Arte

class FormularioArte(forms.ModelForm):
	class Meta:
		model = Arte
		fields = ["nombre","descripcion"]