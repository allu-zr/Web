import streamlit as st
import datetime

import streamlit as st

st.title("Welcome")

name = st.text_input("Entha peru?.")

if name:
    st.write(f"Hello {name},Sughamano?")
    reply = st.text_input("Reply:")
    if reply:
      choice = st.radio(f"Oru Magic aayalo!?", ["OK", "NO"], index=None)

      if choice == "OK":
        dob = st.date_input(
            "Date of Birth Parayamo?",
            value=None,
            min_value=datetime.date(1950, 1, 1),
            max_value=datetime.date(2050, 12, 31),
            help="Vegam para",
        )
        if dob:
          target_date = st.date_input(
              "Innathe Date um koode parayoo",
              value=None,
              min_value=datetime.date(1950, 1, 1),
              max_value=datetime.date(2050, 12, 31),
              help="Innathe Date aane..",
          )
          if target_date:
            if dob <= target_date:
              age = (
                  target_date.year
                 - dob.year
                 - (
                     (target_date.month, target_date.day)
                     < (dob.month, dob.day)
                 )
              )
              st.success(f"Ninte Vayassu {age} Alle?!.")
            else:
              st.error(
                  "Date onnude check cheythu nokku!"
              )
