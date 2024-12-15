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
    # Retorne todos os campos necessários para o modal
    data = list(resultados.values('descricao', 'codigo_do_produto', 'quantidade', 'valor_unitario', 'valor'))
    return JsonResponse(data, safe=False)
from django.shortcuts import render

def pedido(request):
    return render(request, 'busca/pedido.html')  # Certifique-se de que o template está no diretório correto