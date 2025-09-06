import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="🏟️",
    layout="wide"
)

if "data" not in st.session_state:
    st.error("Os dados ainda não foram carregados. Volte para a página inicial (Home).")
    st.stop()

df_data = st.session_state["data"]

# Sidebar - escolha de clube
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

# Filtrar jogadores do clube selecionado
df_filtered = df_data[df_data["Club"] == club].set_index("Name")

# Exibir logo e título do clube
st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

# Colunas a serem mostradas
columns = [
    "Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined",
    "Height(cm.)", "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"
]

st.dataframe(
    df_filtered[columns],
    column_config={
        "Overall": st.column_config.ProgressColumn(
            "Overall", format="%d", min_value=0, max_value=100
        ),
        "Wage(£)": st.column_config.ProgressColumn(
            "Weekly Wage", format="£%f",
            min_value=0, max_value=df_filtered["Wage(£)"].max()
        ),
        "Photo": st.column_config.ImageColumn(),
        "Flag": st.column_config.ImageColumn("Country"),
    }
)
