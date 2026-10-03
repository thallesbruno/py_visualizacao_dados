# Formatação de saídas em Python

# 1. print(): exibe valores separados por um espaço (mostrado na aula passada)
nome = "Ana"
idade = 20
print("Nome:", nome)  # Nome: Ana
print("Idade:", idade, "anos")  # Idade: 20 anos

# 2. sep: define o separador entre os valores
print("Python", "Java", "C", sep=" | ")  # Python | Java | C
print("26", "09", "2026", sep="/")  # 26/09/2026

# 3. end: define como a saída termina (o padrão é uma quebra de linha)
print("Olá,", end=" ")
print(nome)  # As duas chamadas exibem uma única linha: Olá, Ana

# 4. Caracteres especiais: \n quebra a linha e \t insere uma tabulação
print("Primeira linha\nSegunda linha")
print("Nome:\tAna")
print('Ela disse: "Olá!"')  # Aspas simples permitem incluir aspas duplas

# 5. f-strings: inserem variáveis e expressões entre chaves
print(f"{nome} tem {idade} anos.")  # Ana tem 20 anos.
print(f"No próximo ano, terá {idade + 1} anos.")

# 6. Casas decimais: .2f exibe um número com duas casas decimais
preco = 19.9
media = 8.456
print(f"Preço: R$ {preco:.2f}")  # Preço: R$ 19.90
print(f"Média: {media:.2f}")  # Média: 8.46
# A formatação altera apenas a exibição, sem modificar o valor da variável.
# Por padrão, o separador decimal é o ponto.

# 7. Porcentagem: .1% multiplica por 100 e exibe uma casa decimal e o símbolo %
desconto = 0.15
print(f"Desconto: {desconto:.1%}")  # Desconto: 15.0%

# 8. Zeros à esquerda: 04d exibe um inteiro com no mínimo quatro dígitos
codigo = 7
print(f"Código: {codigo:04d}")  # Código: 0007

# 9. Alinhamento: < à esquerda, > à direita e ^ centralizado
# O número 10 define a largura mínima do campo; as barras mostram seus limites.
print(f"|{nome:<10}|")  # |Ana       |
print(f"|{nome:>10}|")  # |       Ana|
print(f"|{nome:^10}|")  # |   Ana    |

# 10. Exemplo prático: uma pequena tabela de produtos
print(f"{'Produto':<12} {'Preço (R$)':>10}")
print("-" * 23)
print(f"{'Caderno':<12} {15.5:>10.2f}")
print(f"{'Caneta':<12} {2.0:>10.2f}")

# 11. Método format(): outra forma de preencher os espaços entre chaves
print("{} tem {} anos.".format(nome, idade))  # Ana tem 20 anos.
print("Preço: R$ {:.2f}".format(preco))  # Preço: R$ 19.90
