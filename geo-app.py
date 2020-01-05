import streamlit as st
from data_processing import *

st.title("Geo-App")
country = st.selectbox(label='Select country',options=['es', 'fi', 'us', 'de', 'pt']).upper()

data_class = ReadData()
df = data_class.query_by_country(country=country)

st.map(df)

st.write("City locations are provided by https://simplemaps.com/data/, https://simplemaps.com/data/us-cities")
