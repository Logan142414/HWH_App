# HWH App: Predicting Graduation and Preview Period Success

### *Machine Learning Application for HWH Non-Profit*

**Team:** Brandon Feld, Logan Laszewski, Eric Rich, Adam Shirley  (Advisor: Vinayaka Gude)

**Club/Internship:** Elon University, Center for Organizational Analytics (Sept 2024 - May 2025)

---

## Executive Summary

**Business Problem:** Housed, Working, and Healthy (HWH) is a non-profit supporting individuals transitioning into sustained employment. With limited program slots, HWH needed a data-driven approach to determine which applicants are likely to complete their Preview Period and ultimately graduate.

**Solution:** Developed two classification models; one predicting if the Preview Period is passed, and one predicting graduation using historical applicant data, SSF scores, and exploratory analysis. A Streamlit app allows HWH staff to enter applicant data and receive probabilities.

**Impact:** The solution enables HWH to use this "Elon Score" to be a factor to help make admissions decisions, improve program completion rates, and focus resources on candidates most likely to benefit from the program.

---

## Business Problem Context

* **Non-profit relevance:** Only a few applicants can be accepted each month; selecting the right participants is crucial.
* **Operational context:** HWH runs programs Tue-Fri with structured roles (Recruiters, Case Managers, Chefs, Employment Coaches, etc).
* **Predictive Data Use:** Using applicant and early SSF data allows HWH to predict a candidate’s likelihood of success before they are accepted into the program.

---

## Methodology

### **Data**

*Daily mood data, applicant data, student performance data (>120 columns)
*Arizona Self-Sufficiency Scale (AZ SSS) for initial assessments
*Using this data allows HWH to predict a candidate’s likelihood of success before acceptance

### **Modeling**

* Classification Models: XGBoost (Graduation), PyTorch Neural Network (Preview Period >12 days), Random Forest
* Model Development & Evaluation: Cross-validation, SMOTE oversampling, GridSearchCV hyperparameter tuning, H20: Model Selection
* Performance Metrics: Accuracy, F1 score, Precision, Recall, AUC
* Feature Selection & Importance: Exploratory data analysis, SHAP values, domain feature engineering

### **Deployment**

* Streamlit App: Interface to input applicant data and receive probabilistic predictions
* Color coded risk output (high, moderate, low)


---

## Skills Demonstrated

* Python data cleaning and preprocessing (Pandas, NumPy)
* Exploratory data analysis and feature selection
* End-to-end machine learning workflow (modeling, evaluation, tuning, feature importance)
* Presenting insights and predictions to nontechnical leadership

---

## Results & Business Recommendations

* Identified key features impacting Preview Period and Graduation success
* Delivered a tool to guide admissions decisions 
* Provided insights for improving data collection and tracking early signals of success
* Future recommendations include integrating early mood data and enabling CSV batch input for applicants in the Streamlit app

---

## Documents

* **Project Overview:** [HWH Project Overview.pdf](Project%20and%20HWH%20Overview.pdf)
* **Streamlit App:** https://hwhelonscore.streamlit.app/

---

## Acknowledgements

* Housed, Working, and Healthy (HWH) staff and leadership
* Elon University Center for Organizational Analytics
* Team and mentors
