## Logistic Regression Model for Credit Risk Assessment
### [https://riskmodellingappclassification.streamlit.app/](https://riskmodellingappclassification.streamlit.app/)

### Overview

This project builds a Logistic Regression model to assess credit risk. The dataset was cleaned and preprocessed to handle missing values and outliers, followed by exploratory data analysis (EDA) and bivariate analysis. Key feature engineering techniques, including interaction terms, were applied.

Feature selection was performed using Variance Inflation Factor (VIF) and Weight of Evidence (WOE) / Information Value (IV) metrics. To address class imbalance, SMOTETomek was employed, improving the model’s recall to 0.94. The final model was validated using ROC-AUC, KS, and Gini metrics to ensure robust credit risk assessment. The model is deployed using Streamlit for easy access and visualization.

### Dataset

Source: The dataset used in this project is sourced from an open-source GitHub repository containing anonymized financial data for credit risk assessment.

Description: Contains customer data, loan details, and credit bureau records.

### Methodology

1. Data Cleaning: Handled missing values and outliers.
2. Exploratory Data Analysis (EDA):
  Univariate and bivariate analysis.
  Distribution analysis of key features.
3. Feature Engineering:
  Created interaction terms.
4.Feature Selection:
  Used VIF to remove multicollinearity.
  Applied WOE/IV for feature importance.
5. Handling Imbalanced Data:
  Used SMOTETomek to balance classes.
6. Model Training:
  Trained a Logistic Regression model.
7. Model Evaluation:
  Used ROC-AUC, KS, and Gini metrics.
  Achieved 0.94 recall.

### Model Performance

Metric      Score
Recall      0.94
ROC-AUC     0.98
KS Stat     0.86
Gini Coeff  0.96

### Deployment

The model is deployed using Streamlit.

To run the Streamlit app: 
[https://riskmodellingappclassification.streamlit.app/](https://riskmodellingappclassification.streamlit.app/)
