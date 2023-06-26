import streamlit as st
import plotly.express as px
from backend import get_data

# The Title
st.title('Weather Forecast for the Next Days')

# Place variable stored as the user inputs
place = st.text_input('Place')

# Slider (forecast days)
days = st.slider('Forecast Days', min_value=1, max_value=5, help='Select the Number of days forecasted')

# Drop down (2 options data to view)
dataType = st.selectbox('Select Data to view', ('Temperature', 'Sky'))

# Dynamic Subheader
st.subheader(f"{dataType} for the next {days} in {place}")


# Adding the graph
# Creating a plotly figure

dates = ['2022-07-08', '2020-04-02', '2021-09-10']

# back-end function to get data
data = get_data(place, days, dataType)

figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature'})
st.plotly_chart(figure)
