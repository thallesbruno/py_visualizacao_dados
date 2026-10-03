import streamlit as st
import pandas as pd

pd.DataFrame(
    {'Lista de Frutas': ["laranja", "limão", "melão"]}
    )

st.title("Opa, Streamlit!")

st.subheader("Uma aplicação Streamlit simples.")

st.table(pd)