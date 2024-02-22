import streamlit as st
from PIL import Image

st.title("Mi primera app!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para intertfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('mago2.jpg')

st.image(image, caption = 'mago')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es:', texto)

st.subheader("AHora usamos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')


