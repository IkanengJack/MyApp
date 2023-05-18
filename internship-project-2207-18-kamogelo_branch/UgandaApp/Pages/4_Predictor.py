import streamlit as st 

import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso

import streamlit as st
import pandas as pd
from sklearn.linear_model import Lasso

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
