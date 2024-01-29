# import and set up streamlit app
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Zena's Amazing Athleisure Catalog")


 
# get list f sweatshirts
with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT color_or_style FROM zenas_athleisure_db.products.catalog_for_website")
    my_cur.fetchall() # all lines
  	 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_catalog = pandas.DataFrame(my_cur.fetchall())
    my_cnx.close()



# add widget for sweatshirt selection
sweater_selected = streamlit.selectbox("Pick an item", my_catalog[0].values.tolist())


# get data matching the selected sweatshirt
# get list f sweatshirts
with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT direct_url, price, size_list, upsell_product_desc  FROM zenas_athleisure_db.products.catalog_for_website WHERE color_or_style = "+sweater_selected + ";")
    my_cur.fetchall() # all lines
  	 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_sweater_data = pandas.DataFrame(my_cur.fetchone())
    my_cnx.close()

# show picture of sweatshirt
streamlit.image(
    my_sweater_data[0],
    width=400,
    caption= "Our warm, comfortable, ' + sweater_selected + ' sweatsuit!" 
)


# price

# available sizes

# additions
