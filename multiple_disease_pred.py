# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 16:13:06 2025

@author: DELL
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loding the files
diabetes_model = pickle.load(open('trained_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_pred_model.sav', 'rb'))


# side bar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple disease prediction system',
                           ['Diabetes Prediction', 
                            'Heart Disease Prediction'],
                           icons =['activity', 'heart'],
                           default_index= 0 )
    

#diabets prediction page
if (selected == 'Diabetes Prediction'):
    #page title
    st.title(' Diabetes prediction using ML')
    
    
    #getting input data from user
    # columns for input fields
    
    col1, col2, col3 = st. columns(3)
    
    with col1:
        Pregnancies = st.text_input('No.of pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood pressure level')
    with col1:
        SkinThickness = st.text_input('skein thickness value')
    with col2:
        Insulin = st.text_input('Insulin value')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes pedigree value')
    with col2:
         Age = st.text_input('Age of the person')
    
    
    
 #code for prediction
    diagnosis = ''
    
    #creating a button for prediction 
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_model([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        if (diagnosis[0]== 1):
            diagnosis = ' The person is diabetic'
            
        else:
            diagnosis = 'The Person is not diabetic'
        
        
        
  
    st.success(diagnosis)
    
    

    
    
if (selected == 'Heart Disease Prediction'):
    #page title
    st.title(' Heart Disease Prediction using ML')
    
    age = st.text_input('age of person')
    sex = st.text_input('sex')
    cp = st.text_input('cp value')
    trestbps = st.text_input('trestbps value')
    chol = st.text_input('chol value')
    fbs = st.text_input('fbs value')
    restecg = st.text_input('restecg value')
    thalach = st.text_input('thalach value')
    exang = st.text_input('exang')
    oldpeak =st.text_input('oldpeak value')
    slope =st.text_input('slope value')
    ca =st.text_input('ca value')
    thal =st.text_input('thal value')

 # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
