from django.shortcuts import render, HttpResponse

# Create your views here.


layout = """
    <h1> Proyecto Web (LP3 - 2024) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango"> Mostrar Números [a,b]</a>
        </li>
    </ul>
    <hr/>
"""



def index(request):
    return render(request,'index.html')


def saludo(request):
    return render(request,'saludo.html')


def rango(request):
    a = 10
    b = 20
    resultado = f"""
        <h2> Numeros de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """   
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout+resultado)


def integrantes(request):
    return render(request,'integrantes.html')



def calculadora(request):
    mensaje = """
        <h1>Calculadora Básica</h1>
        <form method="post">
            <label for="numero1">Número 1:</label><br>
            <input type="number" id="numero1" name="numero1"><br>
            <label for="operacion">Operación:</label><br>
            <select id="operacion" name="operacion">
                <option value="+">Suma</option>
                <option value="-">Resta</option>
                <option value="*">Multiplicación</option>
                <option value="/">División</option>
            </select><br>
            <label for="numero2">Número 2:</label><br>
            <input type="number" id="numero2" name="numero2"><br>
            <input type="submit" value="Calcular">
        </form>
        {% if resultado %}
            <h2>El resultado es: {{ resultado }}</h2>
        {% endif %}
    """
    if request.method == "POST":
        numero1 = int(request.POST["numero1"])
        operacion = request.POST["operacion"]
        numero2 = int(request.POST["numero2"])
        if operacion == "+":
            resultado = numero1 + numero2
        elif operacion == "-":
            resultado = numero1 - numero2
        elif operacion == "*":
            resultado = numero1 * numero2
        elif operacion == "/":
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                resultado = "Error: no se puede dividir entre cero"
        return HttpResponse(mensaje.replace("{{ resultado }}", str(resultado)))
    return HttpResponse(mensaje)







