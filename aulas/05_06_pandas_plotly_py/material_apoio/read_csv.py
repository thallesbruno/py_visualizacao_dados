import pandas as pd

# configuração de visualização
# Define o máximo de linhas para exibição (None remove o limite)
# pd.set_option('display.max_rows', None)
pd.options.display.max_rows = 50

# Define o máximo de colunas para exibição (None remove o limite)
pd.set_option('display.max_columns', None)

# Opcional: Define a largura máxima de cada coluna (evita cortar textos longos)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("Iris.csv")
print(df)