# urls.py
from django.urls import path
from . import views  # Importe as views do app

urlpatterns = [
    path('', views.busca_produtos, name='home'),  # Página inicial
    path('pedido/', views.pedido, name='pedido'),  # Página de pedido
    path('api/search', views.busca_produtos_api, name='busca_produtos_api'),  # API de busca
]
