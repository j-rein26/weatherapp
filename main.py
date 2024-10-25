import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast For Upcoming Days")
place = st.text_input("Place: ")
days_choice = st.slider("Days to Forecast",
                        min_value=1, max_value=5, 
                        help="Select the number of forecasted days.")

option = st.selectbox("Select data to view", 
                      ("Temperature", "Weather Conditions"))

st.subheader(f"{option} for the next {days_choice} days in {place}")


data = get_data(place, days_choice, option)

d, t = get_data(days_choice)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)