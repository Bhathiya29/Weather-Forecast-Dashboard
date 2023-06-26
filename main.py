import streamlit as st

# The Title
st.title('Weather Forecast for the Next Days')

# Place variable stored as the user inputs
place = st.text_input('Place')

# Slider (forecast days)
days = st.slider('Forecast Days', min_value=1, max_value=5, help='Select the Number of days forecasted')

# Drop down (2 options data to view)
dataType = st.selectbox('Select Data to view', ('Temperature','Sky'))

# Dynamic Subheader
st.subheader(f"{dataType} for the next {days} in {place}")
