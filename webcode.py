import streamlit as st

name = st.text_input(
    "Enter your name:"
)
if name:
    st.write(f"Hello {name},How are you?")
    reply = st.text_input("Reply:")
    if reply:
      st.write(f"Enna Shari,Bye")
