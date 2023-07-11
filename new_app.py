import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the trained models
diabetes_model = pickle.load(open('Models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('Models/parkinsons_model.sav', 'rb'))

# Create a dictionary to map selected option to corresponding model and feature names
option_model_mapping = {
    'Diabetes Prediction': (diabetes_model, ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']),
    'Heart Disease Prediction': (heart_disease_model, ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']),
    'Parkinsons Prediction': (parkinsons_model, ['fo', 'fhi', 'flo', 'Jitter_percent', 'Jitter_Abs', 'RAP', 'PPQ', 'DDP', 'Shimmer', 'Shimmer_dB', 'APQ3', 'APQ5', 'APQ', 'DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'])
}

# Sidebar option menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction Systems',
                           list(option_model_mapping.keys()),
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Main content based on selected option
if selected in option_model_mapping:
    st.title(selected)
    
    model, feature_names = option_model_mapping[selected]

    # Input fields
    cols = st.columns(len(feature_names))
    input_data = []
    
    for col, feature_name in zip(cols, feature_names):
        input_value = col.text_input(feature_name)
        input_data.append(input_value)

    # Perform prediction
    if st.button(f'{selected} Result'):
        prediction = model.predict([input_data])[0]
        probabilities = model.predict_proba([input_data])[0]
        
        # Diagnosis and probability display
        if prediction == 1:
            diagnosis = f"The person is diagnosed with {selected}"
            probability = probabilities[1]  # Probability of positive class
        else:
            diagnosis = f"The person is healthy, no {selected}"
            probability = probabilities[0]  # Probability of negative class
        
        st.success(diagnosis)
        st.write('Probability:', probability)
