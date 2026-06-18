import streamlit as st
import pickle
import pandas as pd

## Lets load the trained model..
with open("logistic_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Titanic Survival Prediction using Logistic Regression")

st.write("Enter Passenger Details")

Pclass = st.selectbox("Passenger Class", [1,2,3])

Age = st.number_input("Age", min_value = 0.0)

SibSp = st.number_input("Sibilings/Spouses", min_value = 0)

Parch = st.number_input("Parents/Children", min_value = 0)

Fare = st.number_input("Fare", min_value = 0.0)

Gender = st.selectbox("Gender", ["Female", "Male"])

Embarked = st.selectbox("Embarked", ["C", "Q", "S"])


if Gender == "Male" : 
    Sex_male = 1
else:
    Sex_male = 0

if Embarked == "C":
    Embarked_Q = 0
    Embarked_S = 0
elif Embarked == "Q":
    Embarked_Q = 1
    Embarked_S = 0
else:
    Embarked_Q = 0
    Embarked_S = 2

    
input_data = pd.DataFrame({"Pclass" : [Pclass],
                           "Age" : [Age],
                           "SibSp" : [SibSp],
                           "Parch" : [Parch],
                           "Fare" : [Fare],
                           "Sex_male" : [Sex_male],
                           "Embarked_Q" : [Embarked_Q],
                           "Embarked_S" : [Embarked_S]})

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Passenger is likely to Survive")
    else:
        st.error("Passenger is unlikely to Survive")
        
