# En este archivo definimos las rutas del sitio para que podamos navegar.
# La finalidad es conectar una URL con una vista en views.py.
# Importamos admin para habilitar el panel de administracion de Django
# que nos deja gestionar la base de datos desde el navegador sin escribir codigo.
from django.contrib import admin
# Importamos el método path() de Django para definir cada ruta.
# Lo que hace este método es escribir la URL que definimos, 
# para cargar la vista que le corresponde a cada ruta.
from django.urls import path
# Importamos el archivo views.py de nuestra app para poder
# conectar cada ruta con su funcion correspondiente.
from app import views

# Ahora sí, defino las rutas del sitio:
urlpatterns = [
    # Panel de administracion de Django
    path('admin/', admin.site.urls),
    
    # Páginas publicas accesibles sin login: parte estática del menú
    path('', views.catalogo, name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('catalogo/', views.catalogo, name='catalogo'),
    
    # Páginas de autenticación
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Páginas privadas requieren login
    path('perfil/', views.perfil, name='perfil'),
    path('consultas/', views.consultas, name='consultas'),
]