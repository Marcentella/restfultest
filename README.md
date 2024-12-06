# Proyecto Django Rest Framework - API de Gestión de Proyectos

## Descripción

Esta es una aplicación web desarrollada utilizando **Django** y **Django Rest Framework (DRF)** que permite gestionar proyectos a través de una API RESTful. La aplicación proporciona un sistema de autenticación mediante tokens y controles de acceso según los roles de los usuarios (administradores y usuarios autenticados). Los administradores pueden realizar operaciones de creación, actualización y eliminación, mientras que los usuarios autenticados pueden visualizar los proyectos.

Los proyectos contienen los siguientes campos:

- **nombre**: Nombre del proyecto.
- **rut**: RUT (Registro Único Tributario) asociado al proyecto.
- **title**: Título del proyecto.
- **description**: Descripción detallada del proyecto.
- **technology**: Tecnologías utilizadas en el proyecto.

## Instrucciones para ejecutar el proyecto localmente

Sigue estos pasos para ejecutar la aplicación en tu entorno local:

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local:
```bash
cd directorio
```
```bash
git clone https://github.com/Marcentella/restfultest;
```

### 2. Crear y activar un entorno virtual

Crea un entorno virtual para manejar las dependencias del proyecto:

#### En Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### En macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

Instala las dependencias necesarias utilizando `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Realiza las migraciones para configurar la base de datos:

```bash
python manage.py migrate
```

### 5. Crear un superusuario (opcional)

Si deseas acceder al panel de administración de Django, puedes crear un superusuario:

```bash
python manage.py createsuperuser
```

En la dirección /admin/ (ej: http://127.0.0.1:8000/admin/) puedes añadir usuarios con distintos permisos.

### 6. Ejecutar el servidor

Finalmente, ejecuta el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Accede a la aplicación en tu navegador en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Requerimientos

Para ejecutar este proyecto, necesitas tener las siguientes herramientas instaladas en tu entorno:

- **Python 3.12+**
- **Django 4.x**
- **Django Rest Framework**

## URL pública del despliegue

Puedes acceder a la versión desplegada de la aplicación en la siguiente URL:

[**Despliegue en Render**](https://restfultest-z35s.onrender.com)

---

¡Gracias por utilizar este proyecto! Si tienes alguna pregunta o sugerencia, no dudes en abrir un *issue* o contactar conmigo.
