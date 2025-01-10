# importing necessary libraries
import pickle
import streamlit as st
import pandas as pd
import numpy as np

#load the model
classifier = pickle.load(open('finalm.pkl','rb'))


#page configuration
st.set_page_config(page_title = 'Customer Segmentation Web App', layout='centered')
st.title('Customer Segmentation Web App')

# customer segmentation function
def segment_customers(input_data):

    prediction=classifier.predict(pd.DataFrame(input_data, columns=['Income','Kids','Age','Marital_Status','Education']))
    print(prediction)
    pred_1 = 0
    if prediction == 1:
            pred_1 = 'cluster 1'

    elif prediction == 2:
            pred_1 = 'cluster 2'

    elif prediction == 3:
            pred_1 = 'cluster 3'

    elif prediction == 4:
            pred_1 = 'cluster 4'

    return pred_1
def main():

    Income = st.text_input("Type In The Household Income")
    Kids = st.radio ( "Select Number Of Kids In Household", ('0', '1','2','3') )
    Age = st.slider ( "Select Age", 18, 85 )
    Marital_Status = st.radio ( "Livig With Partner?", ('0', '1') )
    Education = st.radio ( "Select Education", ("0","1") )

    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Segment Customer"):
        result=segment_customers([[Income,Kids,Age,Marital_Status,Education]])

    st.success(result)


if __name__ == '__main__':
        main ()
