"""arteycultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url



from arteycultura.views import inicio, enviarCorreo, ingresar,registrarUsuario,salir
from registro.views import registro, ListaActividades as Registros
from arte.views import agregar, ListaActividades as Arte
from deporte.views import agregardeporte, ListaActividades as Deportes

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^registro$",Registros.as_view()),
    url(r"^registro/add$",registro),
    url(r"^$",inicio),
    url(r"^deporte$",Deportes.as_view()),
    url(r"^arte$",Arte.as_view()),
    url(r"^arte/add$", agregar),
    url(r"^deporte/add$", agregardeporte),
    url(r"^correo$",enviarCorreo),
    url(r"^login$",ingresar),
    url(r"^agregar/usuario$",registrarUsuario),
    url(r"^logout$",salir),
]
