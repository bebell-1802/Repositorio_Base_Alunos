import streamlit as st

# Dados de exemplo
generos = ["indie", "rock emo", "pop", "eletronica"]

# Dicionário relacionando gêneros aos seus artistas/músicas
artistas_por_genero = {
    "indie": ["tv girl"],
    "rock emo": ["my chemical romance"],
    "pop": ["Billie Eilish"],
    "eletronica": ["Ic3peak"]
}

st.sidebar.image("sad.png")              

# Selectbox para escolher o gênero
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o artista/música dentro do gênero selecionado
artista_selecionado = None
if genero_selecionado:
    artista_selecionado = st.sidebar.selectbox(
        "Selecione a música/artista:", 
        artistas_por_genero[genero_selecionado]
    )

# Mostrar o artista e gênero selecionados
if genero_selecionado and artista_selecionado:
    st.write(f"**Gênero selecionado:** {genero_selecionado}")
    st.write(f"**Artista/Música selecionada:** {artista_selecionado}")

    # Links para as músicas, conforme seleção
    if genero_selecionado == "indie" and artista_selecionado == "tv girl":
        st.video("https://www.youtube.com/watch?v=PzIXNqpCug0&pp=ygUHdHYgZ2lybA%3D%3D")

    elif genero_selecionado == "rock emo" and artista_selecionado == "my chemical romance":
        st.video("https://www.youtube.com/watch?v=zdBl1Gzu9Ek&pp=ygUlbXkgY2hlbWljYWwgcm9tYW5jZSBpIGRvbid0IGxvdmUgeW91IA%3D%3D")

    elif genero_selecionado == "pop" and artista_selecionado == "Billie Eilish":
        st.video("https://www.youtube.com/watch?v=2UMMNe7EExk&pp=ygULaSBsb3ZlIHlvdSA%3D")

    elif genero_selecionado == "eletronica" and artista_selecionado == "Ic3peak":
        st.video("https://www.youtube.com/watch?v=RFwYlBWHNXo&list=PLxA687tYuMWh0PsGRLNED6vfkTxqEbi2x&index=2&pp=iAQB8AUB")



