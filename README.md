# HWH App: Predicting Graduation and Preview Period Success

### *Machine Learning Application for HWH Non-Profit*

**Team:** Brandon Feld, Logan Laszewski, Eric Rich, Adam Shirley  (Advisor: Vinayaka Gude)

**Club/Internship:** Elon University, Center for Organizational Analytics (Sept 2024 - May 2025)

---

## Executive Summary

**Business Problem:** Housed, Working, and Healthy (HWH) is a non-profit supporting individuals transitioning into sustained employment. With limited program slots (7 per month), HWH needed a data-driven way to decide which applicants are likely to complete their Preview Period (>12 days) and ultimately graduate.

**Solution:** Developed two classification models; one predicting Preview Period success and one predicting graduation using historical applicant data, SSF scores, and exploratory analysis. A Streamlit app allows HWH staff to enter applicant data and receive predictive probabilities.

**Impact:** The solution enables HWH to make informed admissions decisions, improve program completion rates, and focus resources on candidates most likely to benefit from the program.

---

## Business Problem Context

* **Non-profit relevance:** Only a few applicants can be accepted each month; selecting the right participants is crucial.
* **Operational context:** HWH runs programs Tue-Fri with structured roles (Recruiters, Case Managers, Chefs, Employment Coaches, etc).
* **Data-driven need:** Incorporating applicant and early SSF data allows identification of key factors driving student success.

---

## Methodology

### **Data**

* Daily mood data, applicant data, student performance data (>120 columns, some missing values)
* Arizona Self-Sufficiency Scale (AZ SSS) for initial assessments
  
### **Modeling**

* XGBoost Models for Graduation prediction 
* PyTorch Neural Network used for Preview Period (>12 days) classification 
* Data preprocessing, feature selection, and exploratory analysis performed in Python

### **Deployment**

* Streamlit App: Allows staff to enter data and receive predictions 
* Provides probabilistic output with color coded risk (high, moderate, low) 

---

## Skills Demonstrated

* Python data cleaning and preprocessing (Pandas, NumPy) 
* Exploratory data analysis and feature selection
* Machine learning modeling (Regression, XGBoost, PyTorch NN, Random Forest) 
* Presenting results to nontechnical leadership in Denver

---

## Results & Business Recommendations

* Identified key features impacting Preview Period and Graduation success
* Delivered a tool to guide admissions and resource allocation
* Provided insights for improving data collection and tracking early signals of success
* Future recommendations include integrating early mood data and enabling CSV batch input for applicants in the Streamlit app

---

## Documents

* **Project Overview:** [HWH Project Overview.pdf](Project%20and%20HWH%20Overview.pdf)
* **Streamlit App:** [The_Gamblers_Final_Version_1.ipynb](./The_Gamblers_Final_Version_1.ipynb)
* **Data Dictionary & Datasets:** [Dictionary and Data Sets.zip](./Data Sets/Dictionary and Data Sets.zip)

---

## Acknowledgements

* Housed, Working, and Healthy (HWH) staff and leadership
* Elon University Center for Organizational Analytics
* Intern team and mentors
