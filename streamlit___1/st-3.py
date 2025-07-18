import streamlit as st 
import requests 
import pandas as pd

st.header("Weather APP")

API_KEY = "-----"

def search(city):
    api_address = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + API_KEY
    
    response= requests.get(api_address)
    response =response.json()
    
    # st.write(response["list"])
    for i in response["list"]:
        # st.write(i)
        
        day_name= pd.to_datetime(i['dt_txt']).day_name()
        
        st.subheader(i['dt_txt'])
        st.write(day_name)
        st.write(i['main']['temp'])
        st.write(i['weather'][0]['description'])
        # st.write(day_name)
    # return response
    
city_name= st.text_input("Enter city name")

if st.button('Check Weather'):
    ans= search(city_name)
    # st.write(ans)
    
    