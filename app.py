import streamlit as st
import numpy as np
import pickle


model = pickle.load(open("rf.pkl", 'rb'))

st.title('Heart Disease Predictor')

st.write('This app predicts the likelihood of heart disease based on input features.')

age = st.slider('Age', 1, 120, 30)
sex = st.selectbox('Sex', ['Male', 'Female'])
chest_pain_type = st.selectbox('Chest Pain Type', [
                               'Typical Angina (TA)', 'Atypical Angina (ATA)', 'Non-Anginal Pain (NAP)', 'Asymptomatic (ASY)'])
resting_bp = st.slider('Resting Blood Pressure (mm Hg)', 1, 300, 120)
cholesterol = st.slider('Cholesterol (mg/dL)', 1, 1000, 200)
fasting_bs = st.selectbox(
    'Fasting Blood Sugar > 120 mg/dL', ['True (1)', 'False (0)'])
resting_ecg = st.selectbox('Resting Electrocardiographic Results', [
                           'Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
max_hr = st.slider('Maximum Heart Rate Achieved (bpm)', 1, 300, 150)
exercise_angina = st.selectbox(
    'Exercise-Induced Angina', ['Yes (Y)', 'No (N)'])
oldpeak = st.slider(
    'ST Depression Induced by Exercise Relative to Rest', 0.0, 10.0, 0.0)
st_slope = st.selectbox(
    'ST Slope', ['Upsloping (UP)', 'Flat (FLAT)', 'Downsloping (DOWN)'])

def predict():
    sex_map = {'Male': 1, 'Female': 0}
    chest_pain_type_map = {
        'Typical Angina (TA)': 0, 'Atypical Angina (ATA)': 1, 'Non-Anginal Pain (NAP)': 2, 'Asymptomatic (ASY)': 3}
    fasting_bs_map = {'True (1)': 1, 'False (0)': 0}
    resting_ecg_map = {'Normal': 0, 'ST-T Wave Abnormality': 1,
                       'Left Ventricular Hypertrophy': 2}
    exercise_angina_map = {'Yes (Y)': 1, 'No (N)': 0}
    st_slope_map = {'Upsloping (UP)': 0, 'Flat (FLAT)': 1,
                    'Downsloping (DOWN)': 2}

    sex_val = sex_map[sex]
    chest_pain_type_val = chest_pain_type_map[chest_pain_type]
    fasting_bs_val = fasting_bs_map[fasting_bs]
    resting_ecg_val = resting_ecg_map[resting_ecg]
    exercise_angina_val = exercise_angina_map[exercise_angina]
    st_slope_val = st_slope_map[st_slope]

    input_features = np.array([[age, sex_val, chest_pain_type_val,
                              resting_bp, cholesterol, fasting_bs_val, resting_ecg_val, max_hr, exercise_angina_val, oldpeak, st_slope_val]])
    prediction = model.predict(input_features)

#     st.write('Input features:')
#     st.write(f'- Age: {age}')
#     st.write(f'- Sex: {sex}')
#     st.write(f'- Chest Pain Type: {chest_pain_type}')
#     st.write(f'- Resting Blood Pressure (mm Hg): {resting_bp}')
#     st.write(f'- Cholesterol (mg/dL): {cholesterol}')
#     st.write(f'- Fasting Blood Sugar > 120 mg/dL: {fasting_bs}')
#     st.write(f'- Resting Electrocardiographic Results: {resting_ecg}')
#     st.write(f'- Maximum Heart Rate Achieved (bpm): {max_hr}')
#     st.write(f'- Exercise-Induced Angina: {exercise_angina}')
#     st.write(
#         f'- ST Depression Induced by Exercise Relative to Rest: {oldpeak}')
#     st.write(f'- ST Slope: {st_slope}')

#     st.write('Prediction:')
    if prediction[0] == 0:
#         st.write('Based on the input features, you are not likely to have heart disease.')
         st.success('Based on the input features, you are not likely to have heart disease.')
      
    else:
#         st.write('Based on the input features, you are likely to have heart disease.')
        st.error('Based on the input features, you are likely to have heart disease.')
        
        
submit = st.button('Submit', on_click=predict)
