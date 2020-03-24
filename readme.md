# **Get TCDN** 🚀
**Verificación de Status Code y tiempo de respuesta en consultas HTTP**

* App solicitada por TransparentCDN para vacante Python Developer

## Requisitos de instalación 🔧

* **Activar entorno virtual**
```
source <nombre_entorno_virtual>/bin/activate
```

* **Instalar "requirements"**
```
pip install -r requirements.txt
```
* **Lanzar aplicación**
```
python manage.py runserver
```

* **Abrir con el navegador el LocalHost para entrar a la Home**
```
http://127.0.0.1:8000
```
* Endpoint para consultar dominio ----> http://127.0.0.1:8000/?dominio=www.google.com

* Se puede implementar otro parámetro IP a continuación del dominio para que en lugar de usar la resolución DNS del sistema, haga la petición a esa web contra una IP determinada.

  Ejemplo ---> http://127.0.0.1:8000/?dominio=www.google.com&ip=216.58.213.132


## Construido con 🛠️

* [Python](https://www.python.org/) - Programming language v3.7.4
* [Django](https://www.djangoproject.com/) - Framework v3.0.3
* [Skeleton](http://getskeleton.com/) - Framework CSS
* [SQLite](https://www.sqlite.org/index.html) - Database engine

## Desarrollador ⌨️

* **Jesús Villegas** | [GitHub](https://github.com/jvncode) | [LinkedIn](https://www.linkedin.com/in/jes%C3%BAs-villegas-609b71198/)
