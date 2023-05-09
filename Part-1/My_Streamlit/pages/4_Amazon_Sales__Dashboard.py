import streamlit as st
import os
import pandas as pd
from plotly import express as px

st.title(":red[Dashboard]   Amazon Sales Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "amazon_orders.csv")



df = pd.read_csv(DATA_PATH)
df = df.fillna(0)
df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)
df["Tax Charged"] = df["Tax Charged"].str.replace('$','').astype(float)
df['Order Date'] = pd.to_datetime(df['Order Date'])

st.dataframe(df)

#df.plot.bar(x='Order Date', y='Total Charged', rot=90)

#df.plot.bar(x='Order Date', y='Total Charged', rot=90, figsize=(20,10))

fig = px.bar(df, x='Order Date', y='Total Charged')
fig.update_layout(xaxis_tickangle=-90, width=800, height=400)
st.plotly_chart(fig)
