# Este archivo es muy importante porque aca vamos a ir definir la logica de cada pagina del sitio.
# Cada funcion recibe una solicitud HTTP (request) y devuelve una respuesta,
# que puede ser una pagina HTML o una redireccion a otra URL.
from django.shortcuts import render, redirect
# Importamos login, logout y authenticate de Django.
# login: inicia la sesion del usuario guardando una cookie.
# logout: cierra la sesion eliminando la cookie.
# authenticate: verifica si el usuario y contraseña son correctos.
from django.contrib.auth import login, logout, authenticate
# Importamos el modelo User de Django para crear y consultar usuarios.
from django.contrib.auth.models import User
# Importamos IntegrityError para detectar cuando un usuario ya existe en la BD.
from django.db import IntegrityError
# Importamos el modulo requests para consumir la API externa de productos.
import requests
# Importamos nuestro modelo Consulta para guardar y mostrar consultas.
from .models import Consulta
# Importamos nuestro modelo Perfil para guardar cambios y mostrar los datos del usuario.
from .models import Perfil

# --- PAGINAS PUBLICAS ---
def nosotros(request):
    # Renderiza la pagina de informacion de la empresa.
    return render(request, 'nosotros.html')

def catalogo(request):
    # Consume la API externa de FakeStoreAPI para obtener productos de ropa de mujer.
    # requests.get() hace una solicitud HTTP GET a la URL de la API.
    respuesta = requests.get("https://fakestoreapi.com/products/category/women's clothing")
    # Convertimos la respuesta a formato JSON para poder recorrerla en el template.
    productos = respuesta.json()
    return render(request, 'catalogo.html', {'productos': productos})

# --- AUTENTICACION ---

def registro(request):
    # Si el metodo es GET mostramos el formulario vacio.
    if request.method == 'GET':
        return render(request, 'registro.html')
    else:
        # Si el metodo es POST procesamos los datos enviados por el usuario.
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Creamos el usuario con los datos del formulario.
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['email']
                )
                user.save()
                # Iniciamos sesion automaticamente despues del registro.
                login(request, user)
                return redirect('perfil')
            except IntegrityError:
                # Si el usuario ya existe mostramos un mensaje de error.
                return render(request, 'registro.html', {
                    'error': 'El usuario ya existe'
                })
        return render(request, 'registro.html', {
            'error': 'Las contraseñas no coinciden'
        })

def login_view(request):
    # Si el metodo es GET mostramos el formulario de login.
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # authenticate verifica si el usuario y contraseña son correctos.
        try:
            user_obj = User.objects.get(email=request.POST['email'])
            user = authenticate(request, username=user_obj.username, password=request.POST['password'])
        except User.DoesNotExist:
            user = None
        if user is None:
            # Si las credenciales son incorrectas mostramos error.
            return render(request, 'login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            # Si son correctas iniciamos sesion y redirigimos.
            login(request, user)
            return redirect('perfil')

def logout_view(request):
    # Cierra la sesion del usuario y redirige al inicio.
    logout(request)
    return redirect('login')

# --- PAGINAS PRIVADAS ---
def perfil(request):
    # Verifica que el usuario este logueado sino lo lleva a la pagina de login
    if not request.user.is_authenticated:
        return redirect('login')
    # get_or_create crea el perfil si el usuario todavia no tiene uno
    perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            request.user.delete()
            return redirect('home')
        perfil.nombre = request.POST.get('nombre', '')
        perfil.apellido = request.POST.get('apellido', '')
        perfil.calle = request.POST.get('calle', '')
        perfil.altura = request.POST.get('altura') or None
        perfil.entreCalles = request.POST.get('entreCalles', '')
        perfil.localidad = request.POST.get('localidad', '')
        perfil.codigoPostal = request.POST.get('codigoPostal') or None
        perfil.provincia = request.POST.get('provincia', '')
        perfil.pais = request.POST.get('pais', '')
        perfil.save()
        nuevo_username = request.POST.get('username', '').strip()
        if nuevo_username:
            request.user.username = nuevo_username
        request.user.email = request.POST.get('email', '')
        request.user.save()
        return redirect('perfil')
    # Muestra el perfil del usuario logueado.
    return render(request, 'perfil.html', {'perfil': perfil})

def consultas(request):
    # Muestra y gestiona las consultas del usuario logueado.
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'GET':
        # Obtenemos solo las consultas del usuario logueado.
        consultas = Consulta.objects.filter(usuario=request.user)
        producto_seleccionado = request.GET.get('producto', '')
        return render(request, 'consultas.html', {'consultas': consultas, 'producto_seleccionado': producto_seleccionado})
    else:
        # Guardamos la nueva consulta en la base de datos.
        Consulta.objects.create(
            usuario=request.user,
            asunto=request.POST['asunto'],
            producto=request.POST.get('producto', ''),
            mensaje=request.POST['mensaje']
        )
        return redirect('consultas')