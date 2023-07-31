import streamlit
import pandas

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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
