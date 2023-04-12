from django.http import HttpResponse
# REQUEST -> Realizar las peticiones
# HTTPRESPONSE -> Enviar una respuesta
def inicio(request):
    return HttpResponse("Bienvenido, esta es mi primera aplicacion en Django")

def ruta_html(request):
    return HttpResponse("<h1 style='color: blue;'>Este es un texto con la etiquetas H1.</h1>")

def ruta_saludo(request, nombre):
    resultado = f"<h1>Mi nombre es {nombre}, un gusto de conocerte</>"
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