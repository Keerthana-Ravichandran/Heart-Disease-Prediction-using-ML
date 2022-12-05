

import pickle

import streamlit as st

import numpy as np

from streamlit_option_menu import option_menu


heart_disease_model = pickle.load(open('C:/Users/DELL/Desktop/disease prediction/saved models/heart_disease_model.sav', 'rb'))


with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                          
                          ['About CAD prediction','CAD Disease Prediction','Symptoms','Risk factors'],
                          icons=['person','heart','activity'],
                          default_index=0)
    

    
  
if (selected == 'About CAD prediction'):
    
    # page title
    st.title('Coronary Artery Disease')  
     
    st.header('TO KNOW MORE...')
    
    re=st.button('CLICK HERE')
    
    st.write(":smile:")
    
    
    if re:
        st.text('    Coronary artery disease is a common heart condition.')
        st.text(' The major blood vessels that supply the heart (coronary arteries)')
        st.text('struggle to send enough blood, oxygen and nutrients to the heart muscle.')
        st.text(' Cholesterol deposits (plaques) in the heart arteries and inflammation are ')
        st.text('usually the cause of coronary artery disease.')
            
if (selected == 'Symptoms'):
    st.title('Coronary Artery Disease Symptoms')
    st.text(' For many people, the first clue that they have Coronary Artery Disease is a heart attack.')
    st.text('Symptoms of heart attack include:')

    st.text('                1.Chest pain or discomfort (angina)')
    st.text('               2.Weakness, light-headedness, nausea (feeling sick to your stomach), or a cold sweat')
    st.text('               3.Pain or discomfort in the arms or shoulder')
    st.text('                4.Shortness of breath')
    
 
       
    
  
if (selected == 'Risk factors'):  
    st.title('Coronary Artery Disease Risk factors')
    st.write('Coronary artery disease risk factors include:')

    st.subheader('Age:') 
    st.text('Getting older increases the risk of damaged and narrowed arteries.')
    st.subheader('Sex:') 
    st.text('Men are generally at greater risk of coronary artery disease. However, the risk for women increases after menopause.')
    st.subheader('Smoking:') 
    st.text('If you smoke, quit. Smoking is bad for heart health. People who smoke have a  increased risk of heart disease.')
    st.subheader('High blood pressure:') 
    st.text('Uncontrolled high blood pressure can make arteries hard and stiff (arterial stiffness).')
    st.text('The coronary arteries may become narrow, slowing blood flow.')
    st.subheader('Diabetes:') 
    st.text('Diabetes increases the risk of coronary artery disease. ')
    st.subheader('Overweight or obesity:') 
    st.text('Excess body weight is bad for overall health. Obesity can lead to type 2 diabetes and high blood pressure. ')
    st.subheader('Chronic kidney disease:') 
    st.text('Having long-term kidney disease increases the risk of coronary artery disease.')
    st.subheader('Not getting enough exercise:') 
    st.text('Physical activity is important for good health. A lack of exercise  is linked to coronary artery disease .')
    st.subheader('A lot of stress:') 
    st.text('Emotional stress may damage the arteries and worsen other risk factors for coronary artery disease.')
    st.subheader('Unhealthy diet:') 
    st.text('Eating foods with a lot of saturated fat, trans fat, salt and sugar can increase the risk of coronary artery disease.')
    st.subheader('Alcohol use:') 
    st.text('Heavy alcohol use can lead to heart muscle damage. It can also worsen other risk factors of coronary artery disease.')
    st.subheader('Amount of sleep:') 
    st.text('Too little and too much sleep have both been linked to an increased risk of heart disease.')

    
    
    
    
    
    
if (selected == 'CAD Disease Prediction'):
    
    # page title
    st.title('Coronary Artery Disease Prediction ')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')    
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    lst = [[float(i) for i in [age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]if i !=""]]
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    #b = np.array(a, dtype=float) #  convert using numpy
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(lst)                          
        print(heart_prediction)
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    
    