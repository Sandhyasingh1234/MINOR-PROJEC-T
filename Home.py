import streamlit as st
import pandas as pd

st.title("E-COMMERCE DATA ANALYSIS")
st.image("E-Commerce.jpeg")

st.cache_data()
def load():
    df = pd.read_csv('datasets/data.csv')
    return df   

df = load()

if st.checkbox("View Dataset"):
    st.dataframe(df)

# st.write(df.describe())