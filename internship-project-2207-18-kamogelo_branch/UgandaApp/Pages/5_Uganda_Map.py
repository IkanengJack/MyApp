import streamlit as st 
import folium
import streamlit.components.v1 as components

st.title("Uganda Map")
HtmlFile = open("my_map.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 

# Set the desired height and width for the map
height = 500  # adjust the value as needed
width = 800  # adjust the value as needed

components.html(source_code,  height=height, width=width)