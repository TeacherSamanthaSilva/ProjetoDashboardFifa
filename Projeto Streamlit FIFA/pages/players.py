import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

if "data" not in st.session_state:
    st.error("Os dados ainda não foram carregados. Volte para a página inicial (Home).")
    st.stop()

df_data = st.session_state["data"]

# Sidebar - escolha de clube e jogador
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

# Dados do jogador selecionado
player_stats = df_data[df_data["Name"] == player].iloc[0]

# Exibir foto e nome
st.image(player_stats["Photo"])
st.title(player_stats["Name"])

# Informações básicas
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3 = st.columns(3)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100:.2f} m")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.1f} kg")

st.divider()

# Overall
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

# Métricas financeiras
col1, col2, col3 = st.columns(3)
col1.metric("Valor de mercado", f"£ {player_stats['Value(£)']:,}")
col2.metric("Remuneração semanal", f"£ {player_stats['Wage(£)']:,}")
col3.metric("Cláusula de rescisão", f"£ {player_stats['Release Clause(£)']:,}")
