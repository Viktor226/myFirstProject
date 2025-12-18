import streamlit as st 
st.title("My first project")
name = st.text_input("what is your name ?")
if name :
  st.write(f"hello{name}!")
