
import streamlit as st 
import folium
import pandas as pd
import streamlit.components.v1 as components
import toml
import pickle 
import warnings
import os

from pathlib import Path
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.linear_model import Lasso
from streamlit_option_menu import option_menu
from PIL import Image
#st.markdown("<h1 style='color: #67B69B;'>Solution Overview</h1>", unsafe_allow_html=True)
st.set_page_config(page_title = "Uganda App")
#page_icon (":smiley:" )

st.markdown('<link rel="stylesheet" type="text/css" href="static/style.css">', unsafe_allow_html=True)

background_html = """
<style>
[theme]
base="dark"
primaryColor="#fb0a0a"
textColor="#fcdc04"
</style>
"""

# The main function where we will build the actual app
def main():
    """Uganda App"""
    with st.sidebar:
        selection = option_menu(
        menu_title = "Main Menu",
        options = ["Home","About us", "Fibre Optics Advantages","Predictor", "Uganda_Map","Contact Us"],
        icons = ["house", "book", "magic","bar-chart-line","globe-europe-africa", "envelope" ],
        default_index=0
    )
    
    
    if selection == "Home":
        #st.set_page_config(page_title = "Uganda App")
        

        # Use st.markdown() to insert the HTML code
        st.markdown(background_html, unsafe_allow_html=True)

        st.title("Uganda App")
        st.image(os.path.join("UgandaAppFinal","Team.jpg"), width=800)

    		#select = st.sidebar.selectbox("Who we are 🌐",["The Company","Meet the Team"])
    if selection == "About us":
        col1, col2 = st.columns([2, 1])  # Create two equal-width columns
        
		# Fill the first column  
        col1.header("                    ")
        col1.header("                    ")
        col1.header("                    ")
        col1.markdown("<h1 style='color: #fcdc04;'>About Us</h1>", unsafe_allow_html=True)

        # Place the image in the second column
        col2.image(os.path.join("UgandaAppFinal","logo2.png"), width=300)

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
            st.image(os.path.join("UgandaAppFinal","Kamo.jpeg"), width=200,)
        with col2:
            st.subheader("Kamogelo")
            st.info('Team Lead Manager')

        # 2
        col1, col2 = st.columns(2)
        with col1:
            st.image(os.path.join("UgandaAppFinal","Atunima1.jpeg"), width=200)
        with col2:
            st.subheader("Atunima")
            st.info('Lead Data Engineer')

        # 3
        col1, col2 = st.columns(2)
        with col1:
            st.image(os.path.join("UgandaAppFinal","David.jpeg"), width=200)
        with col2:
            st.subheader("David")
            st.info('Senior Data Analyst')

        # 4
        col1, col2 = st.columns(2)
        with col1:
            st.image(os.path.join("UgandaAppFinal","Layo1.jpeg"), width=200)
        with col2:
            st.subheader("Omolayo")
            st.info('Senior Data Scientist')

        # 5
        col1, col2 = st.columns(2)
        with col1:
            st.image(os.path.join("UgandaAppFinal","Jack.jpg"), width=200)
        with col2:
            st.subheader("Ikaneng Jack")
            st.info('Data Scientist')


    if selection == "Fibre Optics Advantages":
        col1, col2 = st.columns([2, 1])  # Create two equal-width columns

        # Fill the first column  
        col1.header("                    ")
        col1.header("                    ")
        col1.header("                    ")
        col1.markdown("<h1 style='color: #fcdc04;'>Solution Overview</h1>", unsafe_allow_html=True)

        # Place the image in the second column
        col2.image(os.path.join("UgandaAppFinal","logo2.png"), width=300)




        st.markdown("<h3 style='color: #9ca69c;'>Fiber optics offers several advantages over traditional methods of data transmission, such as copper wiring. Here are some key advantages of fiber optics:</h3>", unsafe_allow_html=True)
        st.info('''# Advantages of Fiber Optics:

        1. High Bandwidth                     5. Immunity to Electromagnetic 
         - Enables transmission of           Interference
           large amounts of data           - Unaffected by electromagnetic 
         - Ideal for high-speed              interference and radio
           internet, video streaming,        frequency interference
           cloud computing, etc.             (EMI/RFI)
                                           - Can be installed near electrical 
                                             equipment

        2. Fast Data Transmission         6. Secure Data Transmission
         - Light travels at high           - Difficult to tap into transmission 
           speeds through fiber optic        without detection
           cables                          - Highly secure for sensitive 
         - Achieves terabit-per-second       applications
           speeds                          - Used for government communications,
                                             banking transactions, medical data 
                                             transfer
                                            
        3. Long-Distance Transmission     7. Lightweight and Compact
         - Minimal signal degradation       - Lightweight and smaller diameter 
           over long distances                compared to copper wires
         - Connects geographically          - Easier installation and management
           distant locations                - Higher density and efficient use of 
                                              resources
        4. Resistance to Environmental 
           Factors
         - Less susceptible to temperature ,
           fluctuations moisture, and corrosion
         - Suitable for underwater, underground,
           and industrial settings
        ''')
        st.write("")
        st.image(os.path.join("UgandaAppFinal","Image 2.jpeg"), width= 800)
        st.write("")
        #st.image("Image 1.jpeg", width= 800)
				
	# Building a Predictor Page
    if selection == "Predictor":
        import warnings
        warnings.filterwarnings("ignore", message="Trying to unpickle estimator")


        col1, col2 = st.columns([2, 1])  # Create two equal-width columns

        # Fill the first column  
        col1.header("                    ")
        col1.header("                    ")
        col1.header("                    ")
        col1.markdown("<h1 style='color: #fcdc04;'>Predictor</h1>", unsafe_allow_html=True)

        # Place the image in the second column
        col2.image(os.path.join("UgandaAppFinal","logo2.png"), width=300)
        # Load the dataset
        data = pd.read_csv(os.path.join("UgandaAppFinal","df_train.csv"))


        selected_cols = ['Zonning', 'Employment_rate', 'Total_households', 'poverty_index', 'GDP_per_capita']

        # Prepare the features and target variable
        X = data[selected_cols]
        y = data['tests_per_population']

        # Train the model
        model = pickle.load(open("UgandaAppFinal/RF_model_imp_feats.sav", 'rb'))
        model.fit(X, y)

        # Create the Streamlit app
        def main():
            st.title("Predictor App")
            zoning_options = {1:"Rural", 2:"Mixed", 3:"Town", 4:"Urban"}
            
            # Reverse the zoning_options dictionary
            zoning_mapping = {v: k for k, v in zoning_options.items()}
            
            # Collect input from the user
            feature1_label = st.selectbox("Zonning", list(zoning_options.values()), index=0)
            feature1 = zoning_mapping[feature1_label]
            feature2 = st.number_input("Employement rate:", value=0.0)
            feature3 = st.number_input("Total_households:", value=0.0)
            feature4 = st.number_input("poverty_index", value=0.0)
            feature5 = st.number_input("GDP_per_capita($)", value=0.0)

            # Make a prediction using the trained model
            prediction = model.predict([[feature1, feature2, feature3, feature4, feature5]])

            # Display the prediction
            st.write("Prediction:", prediction)

        if __name__ == "__main__":
            main()



	# Building out the "Sentiment Classifier Analysis" page
    if selection == "Uganda_Map":
        col1, col2 = st.columns([2, 1])  # Create two equal-width columns

        # Fill the first column  
        col1.header("                    ")
        col1.header("                    ")
        col1.header("                    ")
        col1.markdown("<h1 style='color: #fcdc04;'>Uganda Map</h1>", unsafe_allow_html=True)

        # Place the image in the second column
        col2.image(os.path.join("UgandaAppFinal","logo2.png"), width=300)
        #st.title("Uganda Map")
        HtmlFile = open("UgandaAppFinal/my_map1.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 

        # Set the desired height and width for the map
        height = 500  # adjust the value as needed
        width = 800  # adjust the value as needed

        components.html(source_code,  height=height, width=width)

	# Building out the "Contact Us" page
    if selection == "Contact Us":	
        options = {
            "Contact Us": lambda: contact_us()
        }

        def contact_us():
            col1, col2 = st.columns([2, 1])  # Create two equal-width columns

            # Fill the first column  
            col1.header("                    ")
            col1.header("                    ")
            col1.header("                    ")
            col1.markdown("<h1 style='color: #fcdc04;'>Uganda Map</h1>", unsafe_allow_html=True)

            # Place the image in the second column
            col2.image(os.path.join("UgandaAppFinal","logo2.png"), width=300)
            #st.image("Ab.jpg", width=450)
            st.header(" Get in touch with us 📩 ")
            contact_form = """
            <form action="https://formsubmit.co/ereshiagabier@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name"required>
                <input type="email" name="email" placeholder="Your email"required>
                <textarea name="message" placeholder="Your message here"></textarea>
                <button type="submit">Send</button>
            </form>
            """
            st.markdown(contact_form, unsafe_allow_html=True)

            def local_css(file_name):
                with open("UgandaAppFinal/static/style.css") as f:

                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

            local_css("static/style.css")
            st.image("UgandaAppFinal/Thank you.jpg", width=700)

        selection = "Contact Us"
        options.get(selection, lambda: None)()

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()