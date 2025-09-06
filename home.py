import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard FIFA",
    page_icon="⚽",
    layout="wide"
)

# garante que os dados sejam carregados uma única vez
if "data" not in st.session_state:
    df_data = pd.read_csv("Projeto Streamlit FIFA\datasets\CLEAN_FIFA23_official_data.csv", index_col=0)
    st.session_state["data"] = df_data
else:
    df_data = st.session_state["data"]

st.title("🏆 Dashboard FIFA")
st.markdown("Bem-vindo ao Dashboard FIFA! Use o menu lateral para navegar entre as análises.")

# Exibir amostra dos dados para confirmação
st.subheader("Pré-visualização dos dados")
st.dataframe(df_data.head())
