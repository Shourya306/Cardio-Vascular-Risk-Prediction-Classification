import pickle
import numpy as np
import pandas as pd
import streamlit as st

model = pickle.load(open('knn_model.pkl','rb'))
data = pd.read_csv('/Users/shouryachalla/Classification_Project/data_cardiovascular_risk.csv')
st.title('Coronary Heart Disease Prediction')
nav = st.sidebar.radio('Navigation',['About','Prediction'])
if nav == 'About':
    st.image('/Users/shouryachalla/Classification_Project/CHD_image.png')
    if st.checkbox('Show Data'):
     st.table(data)
    st.markdown(
        '''**This model predicts wheather an individual is prone to 10 Year CHD or not. 
    
        K-Nearest Neigbhours has been used to make this prediction.**
        '''
    )

if nav == 'Prediction':
    st.title('Model Inputs')
    age,education,sex,is_smoking,cigsPerDay = st.columns(5)
    
    person_age = age.number_input('Age',min_value=1.0, step=1.0)
    person_edu = education.number_input('Education',min_value=1.0,max_value=4.0)
    person_sex = sex.number_input('Sex',min_value=0.0,max_value=1.0)
    person_smoking = is_smoking.number_input('Smoker',min_value=0.0,max_value=1.0)
    person_cigs = cigsPerDay.number_input('Cigs Per Day', min_value=0.0, step=1.0)
    
    BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol = st.columns(5)
    
    person_BPMeds = BPMeds.number_input('BPMeds',min_value=0.0,max_value=1.0,step=0.01)
    person_stroke = prevalentStroke.number_input('PrevalentStroke',min_value=0.0,max_value=1.0)
    person_hyp = prevalentHyp.number_input('prevalentHyp',min_value=0.0,max_value=1.0)
    person_diabetes = diabetes.number_input('diabetes',min_value=0.0,max_value=1.0)
    person_totChol = totChol.number_input('totChol',min_value=0.0,step = 0.01)

    sysBP,diaBP,Bmi,heartRate,glucose = st.columns(5)

    person_sysBP = sysBP.number_input('sysBP',min_value=0.0,step=0.01)
    person_diaBP = diaBP.number_input('diaBP',min_value=0.0,step=0.01)
    person_bmi = Bmi.number_input('Bmi',min_value=0.0,step=0.01)
    person_heartrate = heartRate.number_input('heartRate',min_value=0.0,step=0.01)
    person_glucose = glucose.number_input('glucose',min_value=0.0,step=0.01)

    if st.button('Predict'):
        result = model.predict(np.array([person_age,person_edu,person_sex,person_smoking,person_cigs,person_BPMeds,person_stroke,person_hyp,
        person_diabetes,person_totChol,person_sysBP,person_diaBP,person_bmi,person_heartrate,person_glucose]).reshape(1,-1))
        result_dict = {0:'Not Prone to 10 Year CHD',1:'Prone to 10 Year CHD'}
        st.success(result_dict[person_diabetes])
    else:
        st.error('Please provide the inputs')

