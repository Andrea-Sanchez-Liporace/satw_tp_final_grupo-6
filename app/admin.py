from django.contrib import admin
# Importamos los modelos que queremos ver en el panel de administracion
from .models import Consulta, Perfil

# Registramos los modelos para que aparezcan en el panel admin de Django
admin.site.register(Consulta)
admin.site.register(Perfil)