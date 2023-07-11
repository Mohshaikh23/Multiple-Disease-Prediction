# Multiple Disease Prediction

This is a web application for predicting multiple diseases: diabetes, heart disease, and Parkinson's disease. The application provides a user interface to input relevant features and obtain predictions for each disease.

## Setup

Clone the repository:

```bash
   git clone <(https://github.com/Mohshaikh23/Multiple-Disease-Prediction.git)>
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
streamlit run Multi_disease_check.py
```

Access the application in your web browser at <http://localhost:8501>

Select the disease prediction system from the sidebar.

Diabetes Prediction
Input the number of pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age of the person.
Click the "Diabetes test Result" button to get the prediction.
Heart Disease Prediction
Input various features including age, sex, chest pain type, resting blood pressure, serum cholestoral, fasting blood sugar, and more.
Click the "Heart Disease Result" button to get the prediction.
Parkinson's Prediction
Input various acoustic features related to the voice of the person.
Click the "Parkinson's Test Result" button to get the prediction.
Models
The machine learning models for each disease prediction are trained and saved in the "Models" directory. The models are loaded using pickle for making predictions in the application.

diabetes_model.sav: Saved model for diabetes prediction.
heart_disease_model.sav: Saved model for heart disease prediction.
parkinsons_model.sav: Saved model for Parkinson's disease prediction.
Dependencies
Python 3.9.7
Streamlit 0.87.0
Scikit-learn 1.0.1
Pandas 1.3.4
NumPy 1.21.4
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Feel free to customize the content based on your project's specifics. Make sure to update the `<(https://github.com/Mohshaikh23/Multiple-Disease-Prediction.git)>` placeholder with the actual URL of your Git repository.

Remember to include the appropriate license file (e.g., LICENSE) in your project directory if you choose to use a different license.

Let me know if you need further assistance!
