from flask import Flask, render_template, request        # render_template es un modulo para actulaizar la pag. web constantemente
from models.persona import *  # para llamar a la clase Persona que esta een la carpeta model y se lo importa todo con *
from models.producto import *

app = Flask(__name__)


@app.route('/')
def index():
    datos = {
        'nombre': 'Manuel García',
        'participantes': [
            {'nombre': 'Carlos'},
            {'nombre': 'María'},
            {'nombre': 'Sandra'}
        ]
    }
    return render_template('index.html', data = datos)


@app.route('/persona', methods=["GET", "POST"])
def persona():
    if request.method == "GET":
        return render_template('persona.html', listas = Persona.get_persona())
    elif request.method == "POST":
        datos = request.form
        persona = Persona(datos['nombre'], datos['apellido'], datos['genero'])
        persona.crear_persona()
        return render_template('persona.html', listas = persona.get_persona())
    else:
        return "PETICIÓN ERRONEA"
    

@app.route('/producto', methods=["GET", "POST"])
def producto():
    if request.method == "GET":
        return render_template('producto.html', listas = Producto.get_producto())
    elif request.method == "POST":
        datos = request.form #atributo para q aparezcan los datos enviados en mi pagina
        producto = Producto(datos['categoria'], datos['producto'], datos['precio'], datos['cantidad'], datos['descripcion'])
        # lo almaceno la clase Producto (con argumentos q son los datos y nombres de lo q vamos a llenar igual al html) en variable producto
        producto.crear_producto() ## lamo al metodo crear_producto
        return render_template('producto.html', listas = producto.get_producto()) #para q me muestro en la pagina lo almacenado
    else:
        return "PETICIÓN ERRONEA"




## Comando para ejecutar flask y nos da una ip local es:
## flask --app app.py --debug run





### Framework conjunto de librerias que te permiten hacer trabajo en especifico, por lo general mas referenciado a app de web,
### tiene paquetes para validar formularios web, para validar clases, paquetes para administrar base de datos,
### coneccion directa con formularios html, clases definidas para llamar un conector de multiples db
#### es un GRAN CONJUNTO DE LIBRERIA que permite hacer interaccion desde la pagina web creada en html hasta codigo backend en python

#### Se usa mas Framework por ser mas sencillo el uso de sus clases ya definidas a estar creando clases para crear interpretes de HTML 
#### tiene un modulo para crear base de datos desde cero
### Ayuda bastante a construir paginas web
### Framework en python es: django, anaconda, flask
### tiene librerias de validacion 
