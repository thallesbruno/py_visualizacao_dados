import csv

pessoas = []

with open("/content/drive/MyDrive/Colab Notebooks/nomes.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)  # Ignora o cabeçalho

    for linha in leitor:
        pessoa = (
            linha[0],         # nome
            linha[1],         # sobrenome
            linha[2],         # data_nascimento
            float(linha[3]),  # peso_kg
            float(linha[4])   # altura_m
        )

        pessoas.append(pessoa)

for pessoa in pessoas:
    print(pessoa)