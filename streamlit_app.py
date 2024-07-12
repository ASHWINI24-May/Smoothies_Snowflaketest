# Import python packages
import streamlit as st
from snowflake.snowpark.functions import Col

# Write directly to the app
st.title(":cup_with_straw: Customise Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the Fruits you want in your custom smoothie!
    """)

from snowflake.snowpark.functions import col
cnx= st.connection("snowflake")
session = Cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_List = st.multiselect('choose up to 5 ingredients:'
, my_dataframe
  )

ingredients_string = ''

if ingredients_List: 
   
  ingredients_string = ''
    

for fruit_chosen in ingredients_List:    
    ingredients_string  += fruit_chosen +''     

st.write(ingredients_List)

my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

#st.write(my_insert_stmt)
time_to_insert = st.button('Submit Order')

if time_to_insert:
 session.sql(my_insert_stmt).collect()

if ingredients_string:
  session.sql(my_insert_stmt).collect()
st.success('Your Smoothie is ordered!', icon="✅")

