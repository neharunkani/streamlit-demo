import streamlit as st

st.title("Simple Greeting App")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Welcome to the app.")

age = st.slider("Select your age:", 1, 100, 18)
st.write(f"Your selected age is: {age}")

if st.button("Celebrate!"):
    st.balloons()
    