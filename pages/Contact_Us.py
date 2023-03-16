import streamlit as st
from send_mail import sent_mail

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject:New Mail from {user_email}

From:{user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        sent_mail(message)
        st.info("Your message was sent successfully")