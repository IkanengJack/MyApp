import streamlit as st 
import folium
import streamlit.components.v1 as components

col1, col2 = st.columns([2, 1])  # Create two equal-width columns

# Fill the first column  
col1.header("                    ")
col1.header("                    ")
col1.header("                    ")
col1.markdown("<h1 style='color: #fcdc04;'>Uganda Map</h1>", unsafe_allow_html=True)

# Place the image in the second column
col2.image("logo2.png", width=300)
#st.title("Uganda Map")
HtmlFile = open("my_map.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 

# Set the desired height and width for the map
height = 500  # adjust the value as needed
width = 800  # adjust the value as needed

components.html(source_code,  height=height, width=width)