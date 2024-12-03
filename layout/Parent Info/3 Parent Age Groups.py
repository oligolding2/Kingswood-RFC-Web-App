import streamlit as st
import pandas as pd


banner = "images/parent info/banner.jpg"
st.image(banner)
st.header("Age Groups")

with st.container():
    st.write("The below table gives a visual representation of a child's journey through the rugby age grades.")
    with st.table():
        st.dataframe(
            pd.DataFrame(
                {
                    "Age Group": ["Micros", "Under 7's", "Under 8's", "Under 9's", "Under 10's", "Under 11's", "Under 12 Kinghts", "Under 12 Athenas", "Under 13 Knights",
                                   "Under 14 Athenas", "Under 14 Knights", "Under 15 Knights", "Under 16 Athenas", "Under 16 Knights", "Colts"],
                    "Childs Age": ["4 and 5", "6", "7", "8", "9", "10", "11", "10 to 11", "12", "12 to 13", "13", "14", "14 to 15", "15", "Under 18"],
                    "School Year": ["Reception and Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Year 6", "Year 6 and 7", "Year 7", "Year 8", 
                                    "Year 8 and 9", "Year 9", "Year 10", "Year 10 and 11", "Year 11",""],
                    "Contact or Tag": ["Tag, no Matches", "Tag", "Tag", "Contact", "Contact", "Contact", "Contact", "Contact", "Contact", "Contact",
                                        "Contact", "Contact", "Contact", "Contact", "Contact"]
                }
            )
        )