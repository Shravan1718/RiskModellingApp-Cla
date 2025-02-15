import streamlit as st
import prediction as pd
st.title('Credit Risk Model App')

# Creating columns layout (3 columns)
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgage"])
    loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"])
    income = st.number_input("Income", min_value=1000, step=500)
    
with col2:
    loan_type = st.selectbox("Loan Type", ["Secured", "Unsecured"])
    loan_tenure_months = st.number_input("Loan Tenure (Months)", min_value=6, max_value=360, step=6)
    number_of_open_accounts = st.number_input("Number of Open Accounts", min_value=0, step=1)
    loan_amount = st.number_input("Loan Amount", min_value=1000, step=500)

    # Calculate Loan to Income Ratio
    loan_to_income_ratio = round(loan_amount / income, 2) if income > 0 else 0.0

with col3:
    credit_utilization_ratio = st.number_input("Credit Utilization Ratio", min_value=0.0, max_value=1.0, step=0.05)
    delinquency_ratio = st.number_input("Delinquency Ratio", min_value=0.0, max_value=1.0, step=0.05)
    avg_dpd_per_delinquency = st.number_input("Avg DPD Per Delinquency", min_value=0, step=1)
    # Display the calculated Loan to Income Ratio
    loan_to_income_ratio_display = st.number_input("Loan to Income Ratio", value=loan_to_income_ratio, disabled=True)


input_data = {
        "age": age,
        "residence_type": residence_type,
        "loan_purpose": loan_purpose,
        "loan_type": loan_type,
        "loan_tenure_months": loan_tenure_months,
        "number_of_open_accounts": number_of_open_accounts,
        "credit_utilization_ratio": credit_utilization_ratio,
        "loan_to_income_ratio": loan_to_income_ratio,
        "delinquency_ratio": delinquency_ratio,
        "avg_dpd_per_delinquency": avg_dpd_per_delinquency
    }

# Predict Button
if st.button("Predict"):
    probability, credit_score, rating = pd.predict(input_data)
    st.write(f"Probability to Default: {probability}")
    st.write(f"Credit_score: {credit_score}")
    st.write(f"Rating: {rating}")