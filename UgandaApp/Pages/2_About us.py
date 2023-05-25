import streamlit as st 

col1, col2 = st.columns([2, 1])  # Create two equal-width columns

# Fill the first column  
col1.header("                    ")
col1.header("                    ")
col1.header("                    ")
col1.markdown("<h1 style='color: #fcdc04;'>About Us</h1>", unsafe_allow_html=True)

# Place the image in the second column
col2.image("logo2.png", width=300)

#st.title('About us')

st.markdown('<div style="text-align: right;">', unsafe_allow_html=True)
#st.title("The Company")
st.sidebar.success("Select a page above")
#st.sidebar.selectbox("Who we are 🌐", ["The Company", "Projects", "Meet the Team"])

#st.markdown('<div style="text-align: right;">', unsafe_allow_html=True)
#st.image("logo2.png", width=300)
st.markdown('</div>', unsafe_allow_html=True)
   
#st.image("logo2.png", width=250)

st.header('Who we are')        
st.info("We are a team of data analyst , data engineers and data scientist. We carry out data analysis and machine learning task for clients in different fields using trendy and up-to-date tools that highlight and present the best solutions to their business needs.")
    
st.header("Meet the Team")

# 1
col1, col2 = st.columns(2)
with col1:
    st.image("Kamo.jpeg", width=200,)
with col2:
    st.subheader("Kamogelo")
    st.info('Team Lead Manager')

# 2
col1, col2 = st.columns(2)
with col1:
    st.image("Atunima.jpeg", width=200)
with col2:
    st.subheader("Atunima")
    st.info('Lead Data Engineer')

# 3
col1, col2 = st.columns(2)
with col1:
    st.image("David.jpeg", width=200)
with col2:
    st.subheader("David")
    st.info('Senior Data Analyst')

# 4
col1, col2 = st.columns(2)
with col1:
    st.image("Layo.jpeg", width=200)
with col2:
    st.subheader("Omolayo")
    st.info('Senior Data Scientist')

# 5
col1, col2 = st.columns(2)
with col1:
    st.image("Jack.jpg", width=200)
with col2:
    st.subheader("Ikaneng Jack")
    st.info('Data Scientist')
