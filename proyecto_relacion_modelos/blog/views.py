from django.shortcuts import render, get_object_or_404
from .models import Autor, Entrada

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

def detalle_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    entradas_autor = Entrada.objects.filter(autor=autor)
    return render(request, 'blog/detalle_autor.html', {'autor': autor, 'entradas_autor': entradas_autor})
# Create your views here.
