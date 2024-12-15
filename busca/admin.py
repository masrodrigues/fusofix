from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Use os nomes dos campos atuais no list_display
    list_display = ("codigo_do_produto", "descricao", "quantidade", "valor", "valor_unitario")
