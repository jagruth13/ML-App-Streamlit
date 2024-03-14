import joblib
import streamlit as st
import numpy as np

model_name = 'RF_Loan_model.joblib'
model = joblib.load(model_name)


def prediction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
        if Gender == "Male":
            Gender = 1
        else:
            Gender = 0

        if Married == "Yes":
            Married = 1
        else:
            Married = 0

        if Dependents >= 3:
            Dependents = 3

        if Education == "Graduate":
            Education = 0
        else:
            Education = 1
        
        if Self_Employed == "Yes":
            Self_Employed = 1
        else:
            Self_Employed = 0

        if Credit_History == "Outstanding Loan":
            Credit_History = 1
        else:
            Credit_History = 0   
        
        if Property_Area == "Rural":
            Property_Area = 0
        elif Property_Area == "Semi Urban":
            Property_Area = 1  
        else:
            Property_Area = 2  
        Total_Income =    np.log(ApplicantIncome + CoapplicantIncome)

        prediction = model.predict([[Gender, Married, Dependents, Education, Self_Employed,LoanAmount, Loan_Amount_Term, Credit_History, Property_Area,Total_Income]])
        print(print(prediction))

        if prediction==0:
            pred = "Rejected"

        else:
            pred = "Approved"
        return pred

def main():
    #Frontend
    st.title("Welcome to Loan Application")
    st.header('Please enter your details to proceed with your loan application')
    gender = st.selectbox("Gender",("Male","Female"))
    married = st.selectbox("Married",("Yes","No"))
    dependent = st.number_input("Number of Dependents")
    education = st.selectbox("Education",("Graduate","Not Graduate"))
    self_employeed = st.selectbox("Self Employeed",("Yes","No"))
    applicantincome = st.number_input("Applicant Income")
    coapplicantincome = st.number_input("Coapplicant Income")
    loanamount = st.number_input("Loan Amount")
    loan_amount_term = st.number_input("Loan Amount Term")
    credit_history = st.selectbox("Credit History",("Outstanding Loan","No Outstanding Loan"))
    property_area = st.selectbox("Property Area",("Rural","Urban","Semi Urban"))

    if st.button("Predict"):
        result = prediction(gender,married,dependent,education,self_employeed,applicantincome,coapplicantincome,loanamount,loan_amount_term,credit_history,property_area)

        if result == "Approved":
            st.success("Your loan application is Approved")
        else:
            st.error("Your loan application is Rejected")


if __name__=="__main__":
    main()