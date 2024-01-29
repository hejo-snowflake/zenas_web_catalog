# import and set up streamlit app
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Zena's Amazing Athleisure Catalog")


 
# Snowflake-related functions
def get_snowflake_data():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM zenas_athleisure_db.products.catalog_for_website")
        return my_cur.fetchall() # all lines

# get data
my_catalog = pandas.DataFrame(get_snowflake_data())

# add widget for sweatshirt selection
sweater_selected = streamlit.selectbox("Pick an item", my_catalog[0].values.tolist())
