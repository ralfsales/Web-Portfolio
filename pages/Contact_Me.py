import streamlit as st

from send_email import send_email

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Target the root HTML elements */
    html, body, [class*="css"]  {
        background-color: #f0f0f0;  /* Light gray color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Contact Me 🙋🏼‍♂️")

with st.form(key="email_forms"):
    user_name = st.text_input("Please, provide your name", placeholder="Type your name...")
    user_email = st.text_input("Your email", placeholder="Type your email address...")
    raw_message = st.text_area("And your message to me:")
    message = f"""\
Subject: New email from {user_name}
email: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
