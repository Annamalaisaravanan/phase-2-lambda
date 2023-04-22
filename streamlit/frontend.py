import streamlit as st
import pandas as pd
import pickle
import numpy as np
import requests
import json

# filename = 'finalized_model.sav'
# model = pickle.load(open(filename, 'rb'))

st.title('Iris Flower Prediction Model')

pl = st.number_input(label = 'Petal length',min_value=0.0,max_value=6.0,step=0.1)

pw = st.number_input(label = 'Petal Width',min_value=0.0,max_value=6.0,step=0.1)

sl = st.number_input(label = 'Sepal Length',min_value=0.0,max_value=6.0,step=0.1)

sw = st.number_input(label = 'Sepal Width',min_value=0.0,max_value=6.0,step=0.1)

#lis = np.array([sl,sw,pl,pw]).reshape(1,4)

inputs ={'pl':pl,'pw':pw,'sl':sl,'sw':sw}

submit = st.button('submit')

if submit:
    #  out = model.predict(lis)
    #  st.success('The predicted output is {}'.format(out[0]))

    res = requests.post(url = 'http://127.0.0.1:8000/predict',data=json.dumps(inputs))

    st.success('The predicted output is {}'.format(res.text))
