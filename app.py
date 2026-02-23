import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Titanic Survival Prediction App")
st.write("Predict whether a passenger survived the Titanic disaster")

# User Inputs
pclass = st.selectbox("Passenger Class", [1,2,3])
sex = st.selectbox("Sex", ["male","female"])
age = st.slider("Age", 1, 80, 25)
sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Fare", 0.0, 500.0, 50.0)

# Default Embarked columns
embarked_Q = 0
embarked_S = 1

# Convert categorical input
sex = 0 if sex == "male" else 1

# Create input DataFrame
input_data = pd.DataFrame([[pclass, sex, age, sibsp, parch, fare, embarked_Q, embarked_S]],
                          columns=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked_Q','Embarked_S'])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Passenger Survived ✅")
    else:
        st.error("Passenger Did Not Survive ❌")