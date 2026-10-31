import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup

URL = "https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol"
CABECALHOS = {"User-Agent": "Mozilla/5.0 (aula de scraping)"}


def achar_tabela(sopa, colunas):
    for tabela in sopa.find_all("table", {"class": "wikitable"}):
        for tr in tabela.find_all("tr")[:2]:
            celulas = [c.text.strip() for c in tr.find_all(["th", "td"])]
            if set(colunas[1:]) <= set(celulas):
                return tabela


def tabela_para_dataframe(tabela, colunas):
    linhas = []
    for tr in tabela.find_all("tr"):
        celulas = [c.text.strip() for c in tr.find_all(["th", "td"])]
        if len(celulas) == len(colunas) and celulas[1] != colunas[1]:
            linhas.append(celulas)
    return pd.DataFrame(linhas, columns=colunas)


def ler_resultados(sopa):
    linhas = []
    for tabela in sopa.find_all("table", {"class": "wikitable"}):
        if "Vice-campeão" not in tabela.text or "Detalhes" not in tabela.text:
            continue
        for tr in tabela.find_all("tr"):
            celulas = [c.text.strip() for c in tr.find_all(["th", "td"])]
            if len(celulas) >= 5 and celulas[0][:4].isdigit():
                linhas.append([int(celulas[0][:4]), celulas[1]] + celulas[-3:])
    colunas = ["Ano", "Campeão", "Vice-campeão", "3º lugar", "4º lugar"]
    return pd.DataFrame(linhas, columns=colunas)


def converter_numeros(tabela, colunas):
    for coluna in colunas:
        texto = tabela[coluna].str.replace("–", "-").str.replace("+", "")
        tabela[coluna] = pd.to_numeric(texto, errors="coerce")
    return tabela


@st.cache_data
def carregar_dados():
    resposta = requests.get(URL, headers=CABECALHOS)
    sopa = BeautifulSoup(resposta.text, "html.parser")

    colunas_estado = ["Estado", "Títulos", "Vices", "3º lugar", "4º lugar"]
    por_estado = tabela_para_dataframe(achar_tabela(sopa, colunas_estado), colunas_estado)
    por_estado = converter_numeros(por_estado, colunas_estado[1:])

    colunas_regiao = ["Região", "Títulos", "Vices", "3º lugar", "4º lugar"]
    por_regiao = tabela_para_dataframe(achar_tabela(sopa, colunas_regiao), colunas_regiao)
    por_regiao = converter_numeros(por_regiao, colunas_regiao[1:])

    colunas_cidade = ["Cidade", "Títulos", "Equipes"]
    por_cidade = tabela_para_dataframe(achar_tabela(sopa, colunas_cidade), colunas_cidade)
    por_cidade = converter_numeros(por_cidade, ["Títulos"])

    colunas_ranking = ["Pos.", "Clube", "Pts", "J", "V", "E", "D", "GP", "GC", "SG"]
    ranking = tabela_para_dataframe(achar_tabela(sopa, colunas_ranking), colunas_ranking)
    ranking = converter_numeros(ranking, colunas_ranking[:1] + colunas_ranking[2:])

    resultados = ler_resultados(sopa)

    return por_estado, por_regiao, por_cidade, ranking, resultados


por_estado, por_regiao, por_cidade, ranking, resultados = carregar_dados()


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
    st.write("Os dados são obtidos por web scraping com requests e BeautifulSoup.")

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

st.subheader("Cinco maiores vencedores")

maiores_vencedores = resultados["Campeão"].value_counts().head(5).reset_index()
maiores_vencedores.columns = ["Clube", "Títulos"]

st.bar_chart(maiores_vencedores, x="Clube", y="Títulos")

st.divider()

st.subheader("Desempenho de um time")

times = sorted(set(resultados["Campeão"]) | set(resultados["Vice-campeão"]) | set(resultados["3º lugar"]) | set(resultados["4º lugar"]))
time = st.selectbox("Escolha um time", times, index=times.index("Palmeiras"))

colocacoes = ["Campeão", "Vice-campeão", "3º lugar", "4º lugar"]
vezes = [int((resultados[coluna] == time).sum()) for coluna in colocacoes]

col6, col7 = st.columns(2)

with col6:
    st.metric("Títulos", vezes[0])

with col7:
    st.metric("Vezes entre os 4 primeiros", sum(vezes))

st.write("Evolução dos títulos ao longo dos anos")

evolucao = pd.DataFrame({
    "Ano": resultados["Ano"],
    "Títulos acumulados": (resultados["Campeão"] == time).cumsum()
})
st.line_chart(evolucao, x="Ano", y="Títulos acumulados")

st.write("Desempenho por colocação")

desempenho = pd.DataFrame({
    "Colocação": ["1º lugar", "2º lugar", "3º lugar", "4º lugar"],
    "Vezes": vezes
})
st.bar_chart(desempenho, x="Colocação", y="Vezes")

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