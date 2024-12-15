from django.urls import path
from . import views

urlpatterns = [
    path('', views.busca_produtos, name='busca_produtos'),
    path('api/search', views.busca_produtos_api, name='busca_produtos_api'),
]
