from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def saludo(request):
    return render(request,'saludo.html')
def integrantes(request):
    return render(request,'integrantes.html')








