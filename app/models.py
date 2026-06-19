# En este archivo definimos la estructura de la base de datos del proyecto.
# Cada clase representa una tabla y cada atributo representa un campo de la entidad.
from django.db import models
# Importamos el modelo User de Django
from django.contrib.auth.models import User

# Cada clase que hereda de models.Model se convierte en una tabla en la base de datos. 
# Django crea el SQL.

# Creamos la tabla para guardar datos adicionales del perfil de ususario ya que el propio modelo de Django no los contempla a todos
class Perfil(models.Model):
    # OneToOneField significa que cada usuario tiene exactamente un perfil
    # on_delete=CASCADE significa que si se borra el usuario se borra su perfil tambien
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Campos opcionales (blank=True) porque el usuario los completa despues del registro
    # Definimos 'nombre' como un campo de texto corto con un límite de 50 caracteres.
    nombre = models.CharField(max_length=50, blank=True)
    # Definimos 'apellido' como un campo de texto corto con un límite de 50 caracteres.
    apellido = models.CharField(max_length=50, blank=True)
    # Definimos 'calle' como un campo de texto corto con un límite de 50 caracteres.
    calle = models.CharField(max_length=50, blank=True)
    # Definimos 'altura' como un campo numerico entero
    altura = models.IntegerField(blank=True, null=True)
    # Definimos 'entreCalles' como un campo de texto corto con un límite de 200 caracteres.
    entreCalles = models.CharField(max_length=200, blank=True)
    # Definimos 'localidad' como un campo de texto corto con un límite de 100 caracteres.
    localidad = models.CharField(max_length=100, blank=True)
    # Definimos 'codigoPostal' como un campo numerico entero
    codigoPostal = models.IntegerField(blank=True, null=True)
    # Definimos 'provincia' como un campo de texto corto con un límite de 100 caracteres.
    provincia = models.CharField(max_length=100, blank=True)
    # Definimos 'pais' como un campo de texto corto con un límite de 100 caracteres.
    pais = models.CharField(max_length=100, blank=True)
    # __str__ define que este objeto se ve en el panel de administracion de Django como texto plano.
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
# Creamos la tabla para guardar las consultas de los usuarios
class Consulta(models.Model):
    # Definimos'usuario' como un campo y como una ForeignKey para crear una relacion entre tablas
    # de esta forma cada consulta pertenece a un usuario. 
    # 'on_delete=CASCADE' significa que si se borra el usuario, se borran todas sus consultas tambien.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # Definimos 'asunto' como un campo de texto corto con un límite de 100 caracteres.
    asunto = models.CharField(max_length=100)
    # Definimos 'producto' como un campo de texto corto con un límite de 100 caracteres.
    # Agregamos default="" para que las consultas que no se generen en base a un prodcuto en especifico queden con texto vacío en este campo.
    producto = models.CharField(max_length=100, default='')
    # Definimos 'mensaje' como un campo de texto largo sin un límite definido.
    mensaje = models.TextField()
    # Definimos 'fecha' con auto_now_add=True que hace que la fecha se complete automaticamente al crear el registro. 
    fecha = models.DateTimeField(auto_now_add=True)
    # __str__ define que este objeto se ve en el panel de administracion de Django como texto plano.
    def __str__(self):
        return f"{self.usuario.username} - {self.asunto}"