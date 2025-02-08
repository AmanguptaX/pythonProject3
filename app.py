import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(name, age, gender, address, datetime, contact):
    sender_email = "crce.9752.ecs@gmail.com"  # Replace with your Gmail
    sender_password = "dqvb vgms jhsr qcbc"  # Replace with your App Password
    receiver_email = "crce.9752.ecs@gmail.com"

    subject = "New Form Submission"
    body = f"""
    Name: {name}
    Age: {age}
    Gender: {gender}
    Address: {address}
    Date & Time: {datetime}
    Contact: {contact}
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False


st.title("Fitnastic health")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
address = st.text_area("Address with Pincode")
datetime = st.text_input("Time & Date")
contact = st.text_input("Contact Number")

if st.button("Submit"):
    if name and age and gender and address and datetime and contact:
        if send_email(name, age, gender, address, datetime, contact):
            st.success("Your form has been submitted successfully!")
        else:
            st.error("Failed to send form. Try again later.")
    else:
        st.warning("Please fill in all required fields.")
