import streamlit as st
from PIL import Image

st.title("MI PORTAFOLIO")

st.header("Camilo Rios Arrieta (AEGIR)")
st.write("Despues lo escribo")
image = Image.open('mago2.jpg')

st.image(image, caption = 'mago')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es:', texto)

st.subheader("Ahora usamos 2 columnas:")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna:")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')

with col2:
  st.subheader("Esta es la segunda columna:")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ('Visual', 'Auditiva', 'Táctil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditiva':
    st.write('La audición es fundamental para tu interfaz')
  if modo == 'Táctil':
    st.write('El tacto es fundamental para tu interfaz')

st.subheader("Uso de botones")
  


