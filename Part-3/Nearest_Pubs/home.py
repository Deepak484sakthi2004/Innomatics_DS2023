import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster

import base64
import os
st.set_page_config(layout="wide")



df = pd.read_csv('cleaned.csv')

st.title("Open Pubs Application")


st.markdown("## :red[About the Dataset]")

st.markdown(" Top Five Rows of Dataset")
st.write(df.head())

st.markdown(" Total Numbers of Rows and Columns")
st.write("Total number of Pubs:", df.shape[0])
st.write("Total number of columns:", df.shape[1])


st.markdown("###### Null Values")
st.write(df.isnull().sum())

st.markdown("###### Duplicated Values")
st.write(df.duplicated().sum())


