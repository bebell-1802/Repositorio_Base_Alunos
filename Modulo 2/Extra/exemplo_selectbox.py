import streamlit as st

# Dados de exemplo
generos = ["indie", "eletronica", "pop", "rock emo"]

# Dicionário relacionando gêneros aos seus livros
musicas = {
    "indie": ["tv girl"],
    "eletronica": ["ic3peak"],
    "pop": ["Billie Eillish", "Lady gaga"],
    "rock emo": ["My chemical romance", "paramore"]
    
}

# Selectbox para escolher o gênero                
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionado = st.sidebar.selectbox(
        "selecione o genero:", 
        generos[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and musicas:
    st.write(f"**musica selecionada:** {musicas}")
    st.write(f"**Gênero:** {genero_selecionado}")
