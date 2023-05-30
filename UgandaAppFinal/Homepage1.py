import streamlit as st 
import folium

from PIL import Image
#st.markdown("<h1 style='color: #67B69B;'>Solution Overview</h1>", unsafe_allow_html=True)
st.set_page_config(page_title = "Uganda App")
#page_icon (":smiley:" )

#st.title("Main Page")
#st.sidebar.success("Select a page above")

# Define the HTML code with the background image
background_image = Image.open("logo 18c.png")

background_html = """
<style>
body {
    background-image: url('logo 18c.png');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
}
</style>
"""

# Use st.markdown() to insert the HTML code
st.markdown(background_html, unsafe_allow_html=True)


st.image("Team.jpg", width= 800)