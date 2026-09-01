import pandas as pd
import joblib


model = joblib.load('insurance_charge_model.pkl')

def predict_charge(age, bmi, children, smoker, region):
    
    smoker_flag = 1 if smoker == 'yes' else 0

  
    smoker_bmi = smoker_flag * bmi

    region_northwest = 1 if region == 'northwest' else 0
    region_southeast = 1 if region == 'southeast' else 0
    region_southwest = 1 if region == 'southwest' else 0

    
    input_data = pd.DataFrame([{
        'age': age,
        'bmi': bmi,
        'children': children,
        'smoker_flag': smoker_flag,
        'smoker_bmi': smoker_bmi,
        'region_northwest': region_northwest,
        'region_southeast': region_southeast,
        'region_southwest': region_southwest,
    }])

 
    predicted_charge = final_model.predict(input_data)[0]
    return round(predicted_charge, 2)
