# import and set up streamlit app
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Zena's Amazing Athleisure Catalog")

# get list f sweatshirts
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT color_or_style FROM zenas_athleisure_db.products.catalog_for_website")
my_catalog = pandas.DataFrame(my_cur.fetchall())




# add widget for sweatshirt selection
sweater_selected = streamlit.selectbox("Pick an item", list(my_catalog[0].values.tolist()))


# get data matching the selected sweatshirt
my_cur.execute("SELECT direct_url, price, size_list, upsell_product_desc  FROM zenas_athleisure_db.products.catalog_for_website WHERE color_or_style =  '" + sweater_selected + "';")
my_sweater_data = my_cur.fetchone()


# show picture of sweatshirt
streamlit.image(
    my_sweater_data[0],
    width=400,
    caption= "Our warm, comfortable, " + sweater_selected + " sweatsuit!" 
)

streamlt.write( my_sweater_data)
streamlt.write( my_sweater_data[1])

# price
streamlit.text('Price:', my_sweater_data[1])

# available sizes
streamlit.text('Sizes Available:', my_sweater_data[2])

# additions
streamlit.text(my_sweater_data[3])



# close connection
my_cnx.close()
