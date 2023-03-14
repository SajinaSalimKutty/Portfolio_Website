import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("Images/IMG.png",width=300)

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index,row in df[0:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index,row in df[3:6].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

