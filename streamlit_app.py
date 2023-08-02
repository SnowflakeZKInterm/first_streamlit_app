import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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


#creating a function for fruityvice
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      # Normalize the api calls response 
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      # Turn/display as the response into a dataframe
  return fruityvice_normalized

  #nEW SECTION FOR FRUITYVICE API RESPONSE
streamlit.header('Fruityvice Fruit Advice!')
try:
    #Text input for getting the user's fruit info
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice: 
    streamlit.error("Please select a fruit to get information.")
      #import requests
  else:
    back_from_function = get_fruityvice_data(fruit_choice) 
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()


  #import snowflake.connector
  #query the metadata
streamlit.header("The fruit load list contains:")
#SF-rlated functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
# add a button to load the fruits
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

  #Allow user to add a fruit
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding '+ new_fruit"
    
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)










