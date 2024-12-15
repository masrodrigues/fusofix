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
    produto = Produto(
        codigo_do_produto=row['codigo_do_produto'],
        descricao=row['descricao'],
        quantidade=row['quantidade'],
        valor=row['valor'],
        valor_unitario=row['valor_unitario']
    )
    produto.save()

print("Dados importados com sucesso!")
