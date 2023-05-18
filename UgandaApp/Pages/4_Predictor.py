import streamlit as st 

import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso

from sklearn.linear_model import Lasso

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
