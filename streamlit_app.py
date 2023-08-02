import streamlit
import pandas
import snowflake.connector

streamlit.title('My Parents New Healthy Diner!')

  #Breakfast menu 🥣 🥗 🐔 🥑🍞
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled, Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

  #Special Header Smoothie
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

  # Display the table on the page.
  #Creating a pandas dataframe and display for it
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

  # Pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

  #Dataframe display
streamlit.dataframe(fruits_to_show)

  #nEW SECTION FOR FRUITYVICE API RESPONSE
streamlit.header('Fruityvice Fruit Advice!')
  #Text input for getting the user's fruit info
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  # Normalize the api calls response 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  # Turn/display as the response into a dataframe
streamlit.dataframe(fruityvice_normalized)
