from django.shortcuts import render, redirect, get_object_or_404
from .models import Peca, DetalhesPeca
from .forms import PecaForm, DetalhesPecaForm
from django.core.paginator import Paginator
from django.contrib import messages



def index(request):
    pecas_list = Peca.objects.all()
    detalhes_pecas_list = DetalhesPeca.objects.all()

    pecas_paginator = Paginator(pecas_list, 2)
    detalhes_paginator = Paginator(detalhes_pecas_list, 2) 

    pecas_page_number = request.GET.get('pecas_page', 1)
    detalhes_page_number = request.GET.get('detalhes_page', 1)

    pecas = pecas_paginator.get_page(pecas_page_number)
    detalhes_pecas = detalhes_paginator.get_page(detalhes_page_number)

    return render(request, 'galeria/index.html', {'pecas': pecas, 'detalhes_pecas': detalhes_pecas})


def cadastro_pecas(request):
    peca_form = PecaForm()
    detalhes_form = DetalhesPecaForm()

    if request.method == 'POST':
        if 'salvar_peca' in request.POST:
            peca_form = PecaForm(request.POST)
            if peca_form.is_valid():
                peca_form.save()
                return redirect('index')
        elif 'salvar_detalhes' in request.POST:
            detalhes_form = DetalhesPecaForm(request.POST)
            if detalhes_form.is_valid():
                detalhes_form.save()
                return redirect('index')

    context = {
        'peca_form': peca_form,
        'detalhes_form': detalhes_form,
    }
    return render(request, 'galeria/cadastro_pecas.html', context)


def editar_peca(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    if request.method == 'POST':
        form = PecaForm(request.POST, instance=peca)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PecaForm(instance=peca)
    return render(request, 'galeria/editar_peca.html', {'form': form})

def editar_detalhes_peca(request, pk):
    detalhes_peca = get_object_or_404(DetalhesPeca, pk=pk)
    if request.method == 'POST':
        form = DetalhesPecaForm(request.POST, instance=detalhes_peca)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DetalhesPecaForm(instance=detalhes_peca)
    return render(request, 'galeria/editar_detalhes_peca.html', {'form': form})

def excluir_peca(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    peca.delete()
    return redirect('index')


def excluir_detalhes_peca(request, pk):
    detalhes_peca = get_object_or_404(DetalhesPeca, pk=pk)
    detalhes_peca.delete()
    return redirect('index')


def realizar_baixa_estoque(request, detalhe_id):
    detalhe = get_object_or_404(DetalhesPeca, pk=detalhe_id)

    if request.method == 'POST':
        quantidade_retirada = int(request.POST.get('quantidade', 0))

        if quantidade_retirada > 0 and detalhe.quantidade_final >= quantidade_retirada:
            detalhe.quantidade_final -= quantidade_retirada
            detalhe.save()
            messages.success(request, f'Sucesso! {quantidade_retirada} unidades retiradas do estoque.')
        else:
            messages.error(request, 'Erro! A quantidade informada é inválida ou maior do que o disponível.')

        return redirect('index')  

    return render(request, 'galeria/realizar_baixa_estoque.html', {'detalhe': detalhe})
