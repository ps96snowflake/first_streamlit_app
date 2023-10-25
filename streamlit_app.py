import streamlit
import pandas as pd

streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑Avacado Toast🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')   

options = streamlit.multiselect('Which beverage do you like?', ['Tea', 'Coffee','Iced Tea' ,'Diet Coke', 'Lemonade'],['Avocado', 'Banana'])

my_fruit_list= pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
selected_fruits=['Apple','Banana']
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),selected_fruits)

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

