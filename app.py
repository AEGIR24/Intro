import streamlit as st
from PIL import Image

st.title("Mi primera app!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para intertfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('mago2.jpg')

st.image(image, caption = 'mago')
