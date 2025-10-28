import streamlit as st
import pandas as pd

#---------confugurações da pagína---------

st.set_page_config(page_title="assassinos em série", page_icon="🩸🔪", layout="wide")

#----------sidebar------------------------

st.sidebar.image("serial-killers.jpg")

#---------título--------------------------

st.title("🔪assassinos e assassinatos🔪")
st.markdown("aqui,todos os piores assassinatos e asassinos do mundo")

#--------menu lateral--------------------

menu = st.sidebar.radio("Escolha",["navegação", "início", "perfis", "Estatísticas", "sobre"])

if menu == "ínicio":
    st.header("bem-vinda criatudas obscuras💀")
    st.write("falamos tudo sobre os assassinos mais insanos")

#--------páginas perfis------------------

elif menu == "perfis":
    st.header("assassinos em série")

    data = {
        "nome": ["Harold Shipman", "Luis Alfredo Garavito", "Ted Bundy"],
     "país": ["Reino Unido", "Colômbia", "EUA"],
     "atividades":["1975-1998", "1992-1999", "1974-1978"],
     "estimativas de assassinato": ["215-250", "190-300", "35-100"],
     "vitimas confirmadas": ["15", "147 crianças", "30 mulheres"],
     "métodos": ["medicamentos/opiáceos (principalmente morfina) por injeção.", "Sequestro, violência sexual, tortura física e estrangulamento ou ferimentos graves", "Sequestro, agressão sexual, estrangulamento e/ou traumatismo craniano."]}
    
    df = pd.DataFrame(data)
    pd.DataFrame(df)

    nome = st.text_input("buscar nome:")
    if nome:
        resultado = df[df["nome"].str.contains(nome,case=False)]
        st.write(resultado if not resultado.empty else "nenhum resultado encontrado.")

