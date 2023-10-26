import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑Avacado Toast🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')   

my_fruit_list= pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include

selected_fruits=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
fruits_to_show=my_fruit_list.loc[selected_fruits]

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    #streamlit.text(fruityvice_response.json())
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  #streamlit.write('The user entered ', fruit_choice)
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information.')
  else:
    streamlit.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
  streamlit.error()
  
streamlit.header("The Fruit load list contains:")
def get_fruit_load_list():
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    mycnx.cursor().execute("select * from pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
    streamlit.dataframe(get_fruit_laod_list())

def insert_row_snowflake(new_fruit):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    query_ins="insert into pc_rivery_db.public.fruit_load_list select '"+str(add_fruit_mylist)+"' where not exists(select 1 from pc_rivery_db.public.fruit_load_list where fruit_name='"+str(add_fruit_mylist)+"')"
    streamlit.write(query_ins) 
    mycnx.cursor().execute(query_ins)
    return 'Thanks for adding'+add_fruit_mylist

try:
  add_fruit_mylist = streamlit.text_input('What fruit would you like to add in list?')
  if not add_fruit_mylist:
    streamlit.error('Please enter a fruit to add in list.')
  else:
    if streamlit.button('Add Fruit in List'):
        streamlit.write(insert_row_snowflake(add_fruit_mylist)) 
except URLError as e:
  streamlit.error()
    
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])    
def snowflake_conn():
    my_cur = my_cnx.cursor()
    my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    my_data_row = my_cur.fetchall()
    streamlit.text(my_data_row)

snowflake_conn()
