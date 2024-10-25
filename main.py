import streamlit as st
import plotly.express as px
from backend import get_data

#add title text, text input, slide, selectbox, and subheader 
st.title("Weather Forecast For Upcoming Days")
place = st.text_input("Place: ")
days_choice = st.slider("Days to Forecast",
                        min_value=1, max_value=5, 
                        help="Select the number of forecasted days.")

option = st.selectbox("Select data to view", 
                      ("Temperature", "Weather Conditions"))

st.subheader(f"{option} for the next {days_choice} days in {place}")

#only call the function if users types a place
if place:
# get the temperature and weather conditions
    filtered_data = get_data(place, days_choice)

    if option == 'Temperature':
        temperatures = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
    #Create temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == 'Weather Conditions':
        images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 
                'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
        weather_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        image_paths = [images[condition] for condition in weather_conditions]
        st.image(image_paths, width=115)