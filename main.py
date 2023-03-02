import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("Images/IMG.png")

with col2:
    st.title("Sajina Salim Kutty")
    content = """
    Hi, I am Sajina Salim Kutty software developer and a teacher.I have completed my graduation in B-Tech (Computer Science) in 2013.
    I have worked in different countries.
    """
    st.info(content)

content2 = """
Below are some of the apps built in python.
"""
st.write(content2)

