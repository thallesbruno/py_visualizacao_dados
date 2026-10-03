# Exemplos de leitura e manipulação de um arquivo CSV.
import csv
from pathlib import Path

# 1. Localizar o CSV na mesma pasta deste script.
arquivo = Path(__file__).parent / "nomes.csv"

# 2. Ler os dados. Cada linha vira um dicionário com os nomes das colunas.
with open(arquivo, encoding="utf-8", newline="") as arquivo_csv:
    pessoas = list(csv.DictReader(arquivo_csv))

# 3. Converter peso e altura: os valores lidos do CSV são textos.
for pessoa in pessoas:
    pessoa["peso_kg"] = float(pessoa["peso_kg"])
    pessoa["altura_m"] = float(pessoa["altura_m"])

# 4. Exibir os nomes completos e contar os registros.
print("Pessoas cadastradas:")
for pessoa in pessoas:
    print(f"{pessoa['nome']} {pessoa['sobrenome']}")

print(f"\nTotal de pessoas: {len(pessoas)}")

# 5. Buscar uma pessoa pelo nome. Troque o valor para experimentar.
nome_buscado = "Ana"
print(f"\nBusca por {nome_buscado}:")
encontrou = False
for pessoa in pessoas:
    if pessoa["nome"].lower() == nome_buscado.lower():
        print(f"Nome: {pessoa['nome']} {pessoa['sobrenome']}")
        print(f"Nascimento: {pessoa['data_nascimento']}")
        encontrou = True

if not encontrou:
    print("Pessoa não encontrada.")

# 6. Filtrar pessoas por altura.
altura_minima = 1.75
print(f"\nPessoas com altura a partir de {altura_minima:.2f} m:")
for pessoa in pessoas:
    if pessoa["altura_m"] >= altura_minima:
        print(f"{pessoa['nome']}: {pessoa['altura_m']:.2f} m")

# 7. Calcular o peso médio.
if pessoas:
    peso_total = 0
    for pessoa in pessoas:
        peso_total += pessoa["peso_kg"]

    peso_medio = peso_total / len(pessoas)
    print(f"\nPeso médio: {peso_medio:.2f} kg")

    # 8. Alterar um valor apenas na memória. O CSV original não é modificado.
    print(f"\nPeso de {pessoas[0]['nome']} antes: {pessoas[0]['peso_kg']:.1f} kg")
    pessoas[0]["peso_kg"] = 63.0
    print(f"Peso após a alteração: {pessoas[0]['peso_kg']:.1f} kg")
