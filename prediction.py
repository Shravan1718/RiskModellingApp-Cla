from joblib import load
import pandas as pd
import numpy as np

model_data = load('artifacts/model_data.joblib')

def generate_rating(score):
    if 300 <= score <500:
        return 'Poor'
    elif 500 <= score <650:
        return 'Average'
    elif 650 <= score <750:
        return 'Good'
    elif 750 <= score <900:
        return 'Excellent'
    else:
        return 'Undefined'

def generate_credit_score(prob):
    return 300 + prob[:,0]*600

def scale_the_df(processed_df):
    scaler = model_data['scaler']
    cols_to_scale = model_data['cols_to_scale']
    columns_to_initialize = [
        'number_of_dependants', 'years_at_current_address',
        'sanction_amount', 'processing_fee', 'gst', 'net_disbursement',
        'principal_outstanding', 'bank_balance_at_application',
        'number_of_closed_accounts', 'enquiry_count'
    ]
    # Set all specified columns to 0
    for col in columns_to_initialize:
        processed_df[col] = 0

    processed_df[cols_to_scale] = scaler.transform(processed_df[cols_to_scale])
    processed_df = processed_df.drop(columns_to_initialize, axis=1)

    return processed_df

def preprocessing(input_data):

    features = model_data['features']
    # i printed this 'features' to display all the required columns
    df = {}

    df['age'] = input_data['age']
    df['loan_tenure_months'] = input_data['loan_tenure_months'] 
    df['number_of_open_accounts'] = input_data['number_of_open_accounts']
    df['credit_utilization_ratio'] = input_data['credit_utilization_ratio']
    df['loan_to_income_ratio'] = input_data['loan_to_income_ratio']
    df['delinquency_ratio'] = input_data['delinquency_ratio']
    df['avg_dpd_per_delinquency'] = input_data['avg_dpd_per_delinquency']

    # Mapping Residence Type
    df["residence_type_Owned"] = 1 if input_data["residence_type"] == "Owned" else 0
    df["residence_type_Rented"] = 1 if input_data["residence_type"] == "Rented" else 0

    # Mapping Loan Purpose
    df["loan_purpose_Education"] = 1 if input_data["loan_purpose"] == "Education" else 0
    df["loan_purpose_Home"] = 1 if input_data["loan_purpose"] == "Home" else 0
    df["loan_purpose_Personal"] = 1 if input_data["loan_purpose"] == "Personal" else 0

    # Mapping Loan Type
    df["loan_type_Unsecured"] = 1 if input_data["loan_type"] == "Unsecured" else 0

    # Convert dictionary to DataFrame
    df = pd.DataFrame([df])

    return df

def predict(data):

    processed_df= preprocessing(data)
    scaled_df = scale_the_df(processed_df)

    model = model_data['model']
    probability = model.predict_proba(scaled_df)

    credit_score = generate_credit_score(probability)
    rating = generate_rating(credit_score)
    
    return f"{np.round(probability[:,1]*100,2)}%", credit_score, rating