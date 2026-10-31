import streamlit as st

st.title("Cadastro de Fornecedores")
st.header("Sistema de Gestão")
st.subheader("Informações Cadastrais")

st.write("Aplicação para gerenciamento de fornecedores.")
st.text("Versão 1.0")
st.caption("Desenvolvido com Python e Streamlit.")

st.divider()

st.info("Preencha os dados para cadastrar um fornecedor.")

with st.container(border=True):
    st.subheader("Informações do Sistema")
    st.write("Os dados serão armazenados em arquivo CSV.")

col1, col2 = st.columns(2)

with col1:
    st.write("Módulo: Fornecedores")

with col2:
    st.write("Armazenamento: CSV")

with st.expander("Orientações de preenchimento"):
    st.write("Informe os dados cadastrais da empresa.")


razao_social = st.text_input("Razão Social")
nome_fantasia = st.text_input("Nome Fantasia")
cnpj = st.text_input("CNPJ")

estado = st.selectbox(
    "Estado",
    ["GO", "DF", "MG", "SP", "RJ"]
)

isento = st.checkbox("Isento de Inscrição Estadual")

if st.button("Testar Cadastro"):
    st.write("Fornecedor:", razao_social)
    st.write("CNPJ:", cnpj)
    st.write("Estado:", estado)
    st.write("Isento:", isento)