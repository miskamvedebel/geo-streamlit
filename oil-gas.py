import streamlit as st
import pandas as pd
import os

DATA_PATH = "test_composition.csv"
DATA_PROD_PATH = "YearlyProduction_table_1.csv.csv"

df = pd.read_csv(DATA_PATH, sep=',')
df = df.rename({'nlat83': 'lat','wlon83': 'lon'}, axis=1)
#df_prod = pd.read_csv(DATA_PROD_PATH)

st.title("Oil and Gas test app")
st.deck_gl_chart(
    viewport={
            'latitude': 37.46,
            'longitude': -82.78,
            'zoom': 11,
            'pitch': 50,
            },
    layers=[{
        'type': 'ScatterplotLayer',
        'data': df
    }]
)


