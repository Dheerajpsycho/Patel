import streamlit as st

# Page Configuration
st.set_page_config(page_title="Fresh Fruits & Vegetables", page_icon="🍎", layout="wide")

# Header
st.title("Welcome to Maa Narmada Fruits, Vegetables and Dairy Products")
st.subheader("Your one-stop destination for farm-fresh produce")

# Section 1: About Us
st.header("About Us")
st.write(
    "We are dedicated to providing you with the freshest and highest quality fruits and vegetables."
    " All our produce is sourced directly from farmers to ensure you enjoy the best nature has to offer."
)

# Section 2: Product Categories
st.header("Our Products")
st.write("We offer a wide variety of fruits and vegetables, including:")

# Columns for Product Categories
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Fresh Fruits")
    st.write("- Apples\n- Bananas\n- Grapes\n- Oranges\n- Mangoes")
    #st.image("https://source.unsplash.com/200x150/?fruits", use_column_width=True)

with col2:
    st.subheader("Fresh Vegetables")
    st.write("- Carrots\n- Spinach\n- Tomatoes\n- Onions\n- Potatoes")
    #st.image("https://source.unsplash.com/200x150/?vegetables", use_column_width=True)

with col3:
    st.subheader("Dairy Products")
    st.write("- Milk\n- Curd\n- Paneer")
    #st.image("https://source.unsplash.com/200x150/?exotic-fruits-vegetables", use_column_width=True)

# Footer
st.markdown("---")
st.title("For inquiries, contact us at \n- **freshproduce@example.com** \n- **+91 9770463018**.")
