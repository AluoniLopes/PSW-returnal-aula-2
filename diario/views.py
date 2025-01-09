from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Pessoa, Diario, models
from datetime import datetime, timedelta

def home(request: HttpRequest):
    pessoas_com_contagem = Pessoa.objects.annotate(qtd_diarios= models.Count('diario'))
    context = dict(
        diarios = Diario.objects.all().order_by('create_at')[:3],
        nomes = [pessoa.nome for pessoa in pessoas_com_contagem],
        qtds = [pessoa.qtd_diarios for pessoa in pessoas_com_contagem]
    )

    return render(request, 'home.html', context)

def escrever(request: HttpRequest):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')
        
        if len(titulo.strip()) == 0 or len(texto.strip()) == 0:
            return redirect('escrever')
        
        diario = Diario(
            titulo=titulo,
            texto=texto
        )
        diario.set_tags(tags)
        diario.save()
        pessoas_obj = Pessoa.objects.filter(id__in=pessoas)
        diario.pessoas.add(*pessoas_obj)

        diario.save()
        return redirect('escrever')
    
    context = dict(
        pessoas = Pessoa.objects.all(),
    )

    #TODO adicionar mensagem de sucesso
    return render(request, 'escrever.html', context)
    
def cadastrar_pessoa(request: HttpRequest):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        pessoa = Pessoa(
            nome=nome,
            foto=foto
        )
        pessoa.save()
        return redirect('escrever')
    return render(request, 'pessoa.html')

def dia(request: HttpRequest):
    data = request.GET.get('data')
    data_formatada = datetime.strptime(data, '%Y-%m-%d')
    diarios = Diario.objects.filter(create_at__gte=data_formatada).filter(create_at__lte=(data_formatada+timedelta(days=1)))
    return render(request, "dia.html", context={'diarios': diarios, 'total': diarios.count(), 'data': data})

def excluir_dia(request: HttpRequest): 
    data = datetime.strptime(request.GET.get('data'), '%Y-%m-%d')
    
    diarios = Diario.objects.filter(create_at__gte=data).filter(create_at__lte=(data+timedelta(days=1)))
    diarios.delete()
    return HttpResponse('teste')