
import streamlit as st 
import folium
import pandas as pd
import streamlit.components.v1 as components

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.linear_model import Lasso
from PIL import Image
#st.markdown("<h1 style='color: #67B69B;'>Solution Overview</h1>", unsafe_allow_html=True)
st.set_page_config(page_title = "Uganda App")
#page_icon (":smiley:" )

# The main function where we will build the actual app
def main():
    options = ["Home","About us", "Fibre_Optics_Advantages","Predictor", "Uganda_Map","Contact Us"]
    selection = st.sidebar.selectbox("Navigation Pane", options)
    if selection == "Home":
        #st.set_page_config(page_title = "Uganda App")
        
        background_html = """
<style>
body {
    background-image: url('Ab.jpg');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
}
</style>
"""

        # Use st.markdown() to insert the HTML code
        st.markdown(background_html, unsafe_allow_html=True)


        st.image("Team.jpg", width= 800)
    		#select = st.sidebar.selectbox("Who we are 🌐",["The Company","Meet the Team"])
    if selection == "About us":
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


    if selection == "Fibre_Optics_Adantages":
        col1, col2 = st.columns([2, 1])  # Create two equal-width columns

        # Fill the first column  
        col1.header("                    ")
        col1.header("                    ")
        col1.header("                    ")
        col1.markdown("<h1 style='color: #fcdc04;'>Solution Overview</h1>", unsafe_allow_html=True)

        # Place the image in the second column
        col2.image("logo2.png", width=300)




        st.markdown("<h3 style='color: #9ca69c;'>Fiber optics offers several advantages over traditional methods of data transmission, such as copper wiring. Here are some key advantages of fiber optics:</h3>", unsafe_allow_html=True)
        st.info('''# Advantages of Fiber Optics:

        1. High Bandwidth             |   4. Immunity to Electromagnetic Interference
        - Enables transmission of         - Unaffected by electromagnetic interference
            large amounts of data             and radio frequency interference
        - Ideal for high-speed              (EMI/RFI)
            internet, video streaming,      - Can be installed near electrical equipment
            cloud computing, etc.

        2. Fast Data Transmission     |    5. Secure Data Transmission
        - Light travels at high            - Difficult to tap into transmission without
            speeds through fiber optic        detection
            cables                            - Highly secure for sensitive applications
        - Achieves terabit-per-second       - Used for government communications,
            speeds                            banking transactions, medical data transfer

        3. Long-Distance Transmission     6. Lightweight and Compact
        - Minimal signal degradation       - Lightweight and smaller diameter compared
            over long distances               to copper wires
        - Connects geographically          - Easier installation and management
            distant locations                 - Higher density and efficient use of resources

        7. Resistance to Environmental Factors
        - Less susceptible to temperature fluctuations,
            moisture, and corrosion
        - Suitable for underwater, underground,
            and industrial settings
        ''')
			
				
	# Building a Predictor Page
    if selection == "Predictor":
        col1, col2 = st.columns([2, 1])  # Create two equal-width columns

        # Fill the first column  
        col1.header("                    ")
        col1.header("                    ")
        col1.header("                    ")
        col1.markdown("<h1 style='color: #fcdc04;'>Predictor</h1>", unsafe_allow_html=True)

        # Place the image in the second column
        col2.image("logo2.png", width=300)
        # Load the dataset
        data = pd.read_csv("df_train.csv")

        selected_cols = ['Total_households', 'rwi', 'Population_density', 'literacy_rate_%', 'Eastern']

        # Prepare the features and target variable
        X = data[selected_cols]
        y = data['uptake_rate']

        # Train the model
        model = Lasso(alpha=0.001)
        model.fit(X, y)

        # Create the Streamlit app
        def main():
            st.title("Predictor App")

            # Collect input from the user
            feature1 = st.number_input("Total_households:", value=0.0)
            feature2 = st.number_input("rwi:", value=0.0)
            feature3 = st.number_input("Population_density:", value=0.0)
            feature4 = st.number_input("Literacy_rate_%", value=0.0)
            feature5 = st.number_input("'Eastern'", value=0.0)

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
        col2.image("logo2.png", width=300)
        #st.title("Uganda Map")
        HtmlFile = open("my_map.html", 'r', encoding='utf-8')
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
            col2.image("logo2.png", width=300)
            #st.title("Uganda Map")
            HtmlFile = open("my_map.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read() 

            # Set the desired height and width for the map
            height = 500  # adjust the value as needed
            width = 800  # adjust the value as needed

            components.html(source_code,  height=height, width=width)
                

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()