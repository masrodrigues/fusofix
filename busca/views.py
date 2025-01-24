from django.shortcuts import render
from .models import Produto
from django.http import JsonResponse

def busca_produtos(request):
    query = request.GET.get('q', '')
    # Atualizar os filtros com os campos corretos do modelo
    resultados = Produto.objects.filter(
        descricao__icontains=query
    ) | Produto.objects.filter(
        codigo_do_produto__icontains=query
    ) if query else []
    return render(request, 'busca/home.html', {'resultados': resultados, 'query': query})
def busca_produtos_api(request):
    query = request.GET.get('q', '')
    resultados = Produto.objects.filter(
        descricao__icontains=query
    ) | Produto.objects.filter(
        codigo_do_produto__icontains=query
    )
    # Retorna mais informações do produto
    data = list(resultados.values(
        'descricao',
        'codigo_do_produto',
        'quantidade',
        'valor',
        'valor_unitario',
        'valor_venda',
        'valor_revenda',
        'valor_atacado'
    ))
    return JsonResponse(data, safe=False)

from django.shortcuts import render

def pedido(request):
    return render(request, 'busca/pedido.html')  # Certifique-se de que o template está no diretório correto