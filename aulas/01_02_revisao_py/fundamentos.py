# Estruturas de Dados em Python

lista_produtos = ["iphone", "ipad", "airpod", "macbook"]
tupla_produtos = ("iphone", "ipad", "airpod", "macbook")
set_produtos = {"iphone", "ipad", "airpod", "macbook"}

# crie:
#    1 lista de itens de sua escolha
#    1 tupla de itens de sua escolha
#    1 set de itens de sua escolha

#    Utilize os métodos de cada estrutura para adicionar, remover e exibir os itens.


# Listas
lista_produtos.append("apple watch")  # Adiciona um item no final da lista (put)
lista_produtos.insert(1, "apple tv")  # Adiciona um item em uma posição específica (put)
lista_produtos.remove("airpod")  # Remove um item da lista (pop)
print(lista_produtos)  # Exibe a lista atualizada

# Tuplas
# Tuplas são imutáveis, então não podemos adicionar ou remover itens
print(tupla_produtos)  # Exibe a tupla
# status, categorias

# Sets
set_produtos.add("apple watch")  # Adiciona um item ao set
set_produtos.remove("airpod")  # Remove um item do set
print(set_produtos)  # Exibe o set atualizado

# Diferenças entre as estruturas:
# - Listas: são mutáveis e permitem duplicatas
# - Tuplas: são imutáveis e permitem duplicatas
# - Sets: são mutáveis e não permitem duplicatas

# Diferenças entre Set e Dicionário:
# - Sets: são coleções não ordenadas de elementos únicos
# - Dicionários: são coleções de pares chave-valor, onde cada chave é única

set_produtos_new = {"iphone", "ipad", "airpod", "macbook"}
dic_produtos = {"iphone": 1500, "ipad": 5000, "airpod": 2000, "macbook": 3000}