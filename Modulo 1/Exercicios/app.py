import streamlit as st

# ---------------------------------------------- SIDEBAR

st.sidebar.image('logo.png')
st.sidebar.title('Cálculo de IMC')


# ---------------------------------------------- PRINCIPAL
st.title('Cálculo de IMC')

peso = st.text_input('Informe seu peso')
altura = st.text_input('Informe sua altura')

if st.button('Calcular'):


    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura ** 2)


    if imc <= 18.5:
        classific = 'Abaixo do peso.'

    elif imc <= 24.9:
        classific = 'Peso normal'    
    elif imc <= 29.9:
        classific = 'Acima do peso'
    elif imc <= 34.9:
        classific = 'Obesidade Grau 1'
    elif imc <= 39.9:
        classific = 'Obesidade Grau 2'
    else:
        classific = 'Obesidade Grau 3'
    
    
    st.warning(f'Seu IMC é: {imc:.2f}. {classific}')