from django.shortcuts import render, redirect
from .models import Projeto, Habilidade
from django.utils import translation

def index(request):
    projetos = Projeto.objects.all()
    habilidades = Habilidade.objects.all()
    return render(request, 'index.html', {
        'projetos': projetos,
        'habilidades': habilidades
    })
"""
def redirect_home(request):
    language = translation.get_language() or 'pt'
    return redirect(f'/{language}/')
"""