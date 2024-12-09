import streamlit as st
from funcs.read_markdown import read_markdown_file

# Read the body markdown content from a file
intro_markdown = read_markdown_file('content/home/club shop/intro.md')


# Specify the path to the banner image
banner = "images/home/banner.jpg"

# Display the banner image at the top of the page
st.image(banner, use_container_width=True)

# Create a container for the welcome message
with st.container():
    # Display a header with a welcome message
    st.header("🛒 The Kingswood Rugby Club Shop!")
    # Display the body markdown content, allowing HTML if present
    st.markdown(intro_markdown, unsafe_allow_html=True)
