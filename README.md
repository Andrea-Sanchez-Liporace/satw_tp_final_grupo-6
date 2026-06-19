# Sarah - Tienda de ropa femenina

Trabajo final para **Seminario de actualización en Tecnología Web**  
Tecnicatura en Análisis de Sistemas · 1er cuatrimestre 2026  
Instituto de Formación Técnica Superior Nº 11 · CABA, Argentina

---

## El proyecto

Sarah es un sitio web de una tienda de ropa femenina desarrollado con Django. Permite a los usuarios registrarse, gestionar su perfil y realizar consultas sobre productos obtenidos de una API externa.

---

## Equipo

| Integrante | Rol |
|---|---|
| Andrea Sanchez Liporace | Fullstack & Diseño |
| Natalia Sanchez Liporace | Frontend & Diseño |
| Sofía Soledad Paez | UX/UI & Diseño |
| Yhosselin Vargas | Frontend & Diseño |

---

## Funcionalidades

- Registro de usuarios con email, usuario y contraseña
- Login con email y contraseña
- Perfil de usuario con edición de datos personales y dirección
- Eliminación de cuenta
- Catálogo de productos consumido desde [FakeStoreAPI](https://fakestoreapi.com)
- Formulario de consultas vinculado a productos del catálogo
- Historial de consultas por usuario
- Página "Nosotras" con presentación del equipo
- Panel de administración Django

---

## Estructura del proyecto
satw_tp_final_grupo-6/
├── tp_web/ # Configuración del proyecto Django
│ ├── settings.py
│ └── urls.py
├── app/ # Aplicación principal
│ ├── models.py # Modelos: Perfil y Consulta
│ ├── views.py # Lógica de cada página
│ ├── admin.py # Registro de modelos en el admin
│ ├── templates/ # Archivos HTML
│ └── static/ # CSS e imágenes
├── manage.py
└── requirements.txt

---
## Tecnologías
- Python 3
- Django 5
- Bootstrap 5
- SQLite
- FakeStoreAPI
---
## Cómo correr el proyecto
1. Clonar el repositorio
2. Crear y activar el entorno virtual
3. Instalar dependencias: `pip install -r requirements.txt`
4. Aplicar migraciones: `python manage.py migrate`
5. Crear superusuario: `python manage.py createsuperuser`
6. Correr el servidor: `python manage.py runserver`
