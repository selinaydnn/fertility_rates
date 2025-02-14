import streamlit as st

st.title("Türkiye Bölgesel Doğurganlık Oranları")

map_path = "turkey_fertility_map.html"
with open(map_path, "r", encoding="utf-8") as f:
    html_code = f.read()

st.components.v1.html(html_code, height=600)

