import streamlit as st
import pickle
import numpy as np

#model import
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))


st.title('Laptop Predictor')

Company=st.selectbox('Brand',df['Company'].unique())

CPU=st.selectbox('CPU',df['CPU'].unique())

Processor=st.selectbox('Processor',df['Processor'].unique())

OS=st.selectbox('OS',df['OS'].unique())

RAM_size=st.selectbox('RAM size(in GB)',df['RAM_size'].unique())

RAM_type=st.selectbox('RAM type',df['RAM_type'].unique())

Memory=st.selectbox('Memory',df['Memory'].unique())

Memory_chips=st.selectbox('Memory chips',df['Memory_chips'].unique())

if st.button('Predict Price'):
    query=np.array([Company,Processor,CPU,OS,RAM_size,RAM_type,Memory,Memory_chips])
    query=query.reshape(1,12)

    st.title("The predicted price is :"+str(int(np.exp(pipe.predict(query)[0]))))