import streamlit as st
from PIL import Image

st.title('サンプルアプリ')
st.caption('これはテストアプリです')

image = Image.open('./data/Git_DL_page.png')
st.image(image, width=200, caption='サンプル画像')