import os
import sys
import django
import pandas as pd

# Adiciona o caminho do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'belenus_project.settings')
django.setup()

# Importar o modelo Produto
from busca.models import Produto

# Caminho do arquivo Excel
excel_file_path = r"C:\Users\marco.rodrigues\Documents\base_belenus.xlsx"

# Ler os dados do arquivo Excel
df = pd.read_excel(excel_file_path)

# Iterar pelos dados e inserir no banco
for _, row in df.iterrows():
    produto_existente = Produto.objects.filter(codigo_do_produto=row['codigo_do_produto']).first()
    
    if produto_existente:
        # Atualizar o registro existente
        produto_existente.descricao = row['descricao']
        produto_existente.quantidade = row['quantidade']
        produto_existente.valor = row['valor']
        produto_existente.valor_unitario = row['valor_unitario']
        produto_existente.valor_venda = row['valor_venda']
        produto_existente.valor_revenda = row['valor_revenda']
        produto_existente.valor_atacado = row['valor_atacado']
        produto_existente.save()
        print(f"Produto atualizado: {row['codigo_do_produto']}")
    else:
        # Criar um novo registro
        produto = Produto(
            codigo_do_produto=row['codigo_do_produto'],
            descricao=row['descricao'],
            quantidade=row['quantidade'],
            valor=row['valor'],
            valor_unitario=row['valor_unitario'],
            valor_venda=row['valor_venda'],
            valor_revenda=row['valor_revenda'],
            valor_atacado=row['valor_atacado']
        )
        produto.save()
        print(f"Produto inserido: {row['codigo_do_produto']}")

print("Importação concluída!")
