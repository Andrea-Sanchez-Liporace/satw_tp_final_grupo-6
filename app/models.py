# En este archivo definimos la estructura de la base de datos del proyecto.
# Cada clase representa una tabla y cada atributo representa un campo de la entidad.
from django.db import models
# Importamos el modelo User de Django
from django.contrib.auth.models import User

# Cada clase que hereda de models.Model se convierte en una tabla en la base de datos. 
# Django crea el SQL.
class Consulta(models.Model):
    # Definimos'usuario' como un campo y como una ForeignKey para crear una relacion entre tablas
    # de esta forma cada consulta pertenece a un usuario. 
    # 'on_delete=CASCADE' significa que si se borra el usuario, se borran todas sus consultas tambien.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # Definimos 'asunto' como un campo de texto corto con un límite de 100 caracteres.
    asunto = models.CharField(max_length=100)
    # Definimos 'mensaje' como un campo de texto largo sin un límite definido.
    mensaje = models.TextField()
    # Definimos 'fecha' con auto_now_add=True que hace que la fecha se complete automaticamente al crear el registro. 
    fecha = models.DateTimeField(auto_now_add=True)
    # __str__ define que este objeto se en el panel de administracion de Django como texto plano.
    def __str__(self):
        return f"{self.usuario.username} - {self.asunto}"