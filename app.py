import streamlit as st
import re
import time
import random
import string

# Set page title
st.title("🔒 Password Strength Checker")

# Create a header 
bar = st.progress(0)
for percent in range(100):
    bar.progress(percent + 1)
    time.sleep(0.01)
st.header("Check the strength of your password")

# Create a form
with st.form("password_form"):
    # Create a text input for password
    password = st.text_input("Enter your password", type="password", placeholder="Minimum 8 characters")

    # Create a checkbox to show password
    show_password = st.checkbox("Show password")

    # Create a submit button
    submit_button = st.form_submit_button("Check Strength")

# Create a container to display results
result_container = st.container()

# Define a function to check password strength
def check_password_strength(password):
    errors = []
    if len(password) < 8:
        errors.append("Password should be at least 8 characters long")
    if not re.search("[a-z]", password):
        errors.append("Password should have at least one lowercase letter")
    if not re.search("[A-Z]", password):
        errors.append("Password should have at least one uppercase letter")
    if not re.search("[0-9]", password):
        errors.append("Password should have at least one number")
    if not re.search("[^A-Za-z0-9]", password):
        errors.append("Password should have at least one special character")
    return errors

# Check password strength when submit button is clicked
if submit_button:
    errors = check_password_strength(password)
    if errors:
        result_container.write("Password strength: Weak")
        for error in errors:
            st.error(error)
    else:
        result_container.write("Password strength: Strong")
        st.success("Password is strong and secure!")

# Add a password generator feature
col1, col2 = st.columns(2)
with col1:
    if st.button("Generate Password"):
        password_length = 12
        generated_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length))
        st.write("Generated Password: ", generated_password)
with col2:
    if st.button("Store Password"):
        # TO DO: Implement password storage logic here
        st.write("Password stored successfully!")
