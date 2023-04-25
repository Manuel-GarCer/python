from django.http import HttpResponse
from django.template import Template, Context, loader

# REQUEST -> Realizar las peticiones
# HTTPRESPONSE -> Enviar una respuesta usando el protocolo HTTP
def inicio(request):
    return HttpResponse("Bienvenido, esta es mi primera aplicacion en Django")

def ruta_html(request):
    return HttpResponse("<h1 style='color: blue;'>Este es un texto con la etiquetas H1.</h1>")

def ruta_saludo(request, nombre):
    resultado = f"<h1>Mi nombre es <span style='color: red;'>{nombre}</span>, un gusto de conocerte</>"
    return HttpResponse(resultado)

def ruta_saludo2(request, nombre, edad):
    resultado = f"<h1>Mi nombre es <span style='color: red;'>{nombre}</span>, un gusto en conocerlos. Y tengo <span style='color: blue;'>{edad}</span> años.</h1>"
    return HttpResponse(resultado)

def ruta_html2(request):
    resultado = f"""
        <h1>Título</h1>
        <p>Parrafo</p>
        <br>
        <span>Span</span>
        <br>
        <ul>
            <li>Lista 01</li>
            <li>Lista 02</li>
            <li>Lista 03</li>
        </ul>
    """
    return HttpResponse(resultado)

def plantilla(request):
    titulo = "Estudiantes"
    lista_estudiantes = [
        {'nombre': 'Manuel', 'matricula': '1'},
        {'nombre': 'Juan', 'matricula': '0'},
        {'nombre': 'Pedro', 'matricula': '1'},
        {'nombre': 'Dayana', 'matricula': '1'},
        {'nombre': 'Luis', 'matricula': '0'}
    ]
    # Abrimos el documento en html:
    template = open('C:/Users/Manolo/Desktop/python/modulo04/sistema_colegio/templates/plantilla01.html')
    # Cargar el documento a la variable read_template
    read_template = Template(template.read())  # (leer plantilla)
    # Cerrando el documento(plantilla01.html) abierto ateriormente
    template.close()
    # Creando un contexto
    context = Context({
        'titulo': titulo,
        'data_alumnos': lista_estudiantes
    })
    # Renderizando el documento(plantilla01.html)
    document = read_template.render(context) # render = renderizando
    return HttpResponse(document)

lista_estudiantes = list()

def plantilla02(request):
    # diferenciando las llamadas desde nuestra plantilla hacia nuestra vista
    # print(request.method)
    # Reciviendo datos desde mi plantilla
    # print(request.GET)  
    # print(request.POST)
    if request.method == 'POST':
        lista_estudiantes.append(request.POST) #con esto evitamos enviar POST en blanco
        
    #Con lo q sigue abrimos directamente la plantilla, lo cargamos a la variable
    template = loader.get_template('plantilla02.html') # loader=cargador del metodo get_template la plantilla02.html
    context = {
        'data_alumnos': lista_estudiantes
    }
    # Renderizando el documento(plantilla01.html)
    document = template.render(context)
    return HttpResponse(document)

def plantilla_heredada(request):
    template = loader.get_template('base.html')
    context = {}
    document = template.render(context)
    return HttpResponse(document)

def view_alumno(request):
    template = loader.get_template('alumno.html')
    context = {}
    document = template.render(context)
    return HttpResponse(document)

def view_asignatura(request):
    template = loader.get_template('asignatura.html')
    context = {}
    document = template.render(context)
    return HttpResponse(document)