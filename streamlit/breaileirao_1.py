import requests
import pandas as pd
import streamlit as st
from io import StringIO

URL = "https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol"
CABECALHOS = {"User-Agent": "Mozilla/5.0 (aula de scraping)"}


@st.cache_data
def carregar_tabelas():
    resposta = requests.get(URL, headers=CABECALHOS)
    return pd.read_html(StringIO(resposta.text))


def achar_tabela(tabelas, colunas):
    for tabela in tabelas:
        if set(colunas) <= set(str(coluna) for coluna in tabela.columns):
            return tabela.copy()
        for posicao, linha in tabela.iterrows():
            if set(colunas) <= set(linha.astype(str)):
                dados = tabela.loc[posicao + 1:].copy()
                dados.columns = [str(coluna) for coluna in linha]
                dados = dados.drop(columns=["nan"], errors="ignore")
                return dados.reset_index(drop=True)


def converter_numeros(tabela, colunas):
    for coluna in colunas:
        texto = tabela[coluna].astype(str).str.replace("–", "-").str.replace("+", "")
        tabela[coluna] = pd.to_numeric(texto, errors="coerce")
    return tabela


tabelas = carregar_tabelas()

por_estado = achar_tabela(tabelas, ["Estado", "Títulos", "Vices"])
por_estado = converter_numeros(por_estado, ["Títulos", "Vices", "3º lugar", "4º lugar"])

por_regiao = achar_tabela(tabelas, ["Região", "Títulos", "Vices"])
por_regiao = converter_numeros(por_regiao, ["Títulos", "Vices", "3º lugar", "4º lugar"])

por_cidade = achar_tabela(tabelas, ["Cidade", "Títulos", "Equipes"])
por_cidade = converter_numeros(por_cidade, ["Títulos"])

ranking = achar_tabela(tabelas, ["Pos.", "Clube", "Pts"])
ranking = converter_numeros(ranking, ["Pos.", "Pts", "J", "V", "E", "D", "GP", "GC", "SG"])


st.title("Dados sobre o Brasileirão - Todos os anos")
st.header("Painel de Estatísticas")
st.subheader("Títulos e pontuação histórica")

st.write("Aplicação para consulta dos dados históricos do Campeonato Brasileiro.")
st.text("Versão 1.0")
st.caption("Desenvolvido com Python e Streamlit.")

st.divider()

st.info("Dados extraídos das tabelas do artigo da Wikipédia sobre o Campeonato Brasileiro de Futebol.")

with st.container(border=True):
    st.subheader("Informações do Sistema")
    st.write("Os dados são obtidos por web scraping com requests e pandas.")

col1, col2 = st.columns(2)

with col1:
    st.write("Módulo: Estatísticas")

with col2:
    st.write("Fonte: Wikipédia")

with st.expander("Orientações de uso"):
    st.write("Escolha uma opção abaixo e clique em Atualizar para ver os resultados.")

st.divider()

st.subheader("Indicadores")

estado_lider = por_estado.sort_values("Títulos", ascending=False).iloc[0]
clube_lider = ranking.sort_values("Pts", ascending=False).iloc[0]

col3, col4, col5 = st.columns(3)

with col3:
    st.metric("Estado com mais títulos", estado_lider["Estado"], int(estado_lider["Títulos"]))

with col4:
    st.metric("Líder do ranking histórico", clube_lider["Clube"], int(clube_lider["Pts"]))

with col5:
    st.metric("Estados com algum título", int((por_estado["Títulos"] > 0).sum()))

st.divider()

visao = st.selectbox(
    "Visão",
    ["Por estado", "Por região", "Por cidade", "Ranking histórico"]
)

mostrar_grafico = st.checkbox("Mostrar gráfico", value=True)

if st.button("Atualizar"):
    st.subheader(visao)

    if visao == "Por estado":
        st.dataframe(por_estado)
        if mostrar_grafico:
            st.bar_chart(por_estado, x="Estado", y="Títulos")

    elif visao == "Por região":
        st.dataframe(por_regiao)
        if mostrar_grafico:
            st.bar_chart(por_regiao, x="Região", y="Títulos")

    elif visao == "Por cidade":
        st.dataframe(por_cidade)
        if mostrar_grafico:
            st.bar_chart(por_cidade, x="Cidade", y="Títulos")

    else:
        st.dataframe(ranking)
        if mostrar_grafico:
            st.bar_chart(ranking.head(10), x="Clube", y="Pts")