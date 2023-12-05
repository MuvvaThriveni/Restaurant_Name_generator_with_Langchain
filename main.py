import streamlit as st
import langchain_helper
import pycountry

# Set page configuration
st.set_page_config(
    page_title="Restaurant Name Generator",
    page_icon=":fork_and_knife:",
    layout="wide"
)

# Add a background image
background = """ 
<style>
body {
    background-image: url('https://thumbs.dreamstime.com/b/empty-wooden-table-top-blurred-restaurant-cafe-light-bac-background-can-be-used-product-display-97966416.jpg');
    background-size: cover;
    
}
</style>
"""
# Display the background image
st.markdown(background, unsafe_allow_html=True)


st.title("Restaurant Name Generator")

# Get all country names using pycountry
all_countries = [country.name for country in pycountry.countries]

# Add an option for "All" cuisines
cuisine_options = ["All"] + all_countries

cuisine = st.sidebar.selectbox("Pick a Cuisine", cuisine_options)

if cuisine and cuisine != "All":
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)
elif cuisine == "All":
    # Display all countries
    st.write("All country names:")
    st.write(all_countries)
