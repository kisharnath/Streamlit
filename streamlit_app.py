import streamlit as st
st.title("Compare three numbers")
number1 = st.number_input("Insert a number", key="number1", value=None, placeholder="Type a number...")
number2 = st.number_input("Insert a number",  key="number2",value=None, placeholder="Type a number...")
number3 = st.number_input("Insert a number", key="number3", value=None, placeholder="Type a number...")
button = st.button("Compare")
if button:
  if number1 > number2 :
    if number3 > number1 :
      st.write("Largest number",number3)
    else:
      st.write("Larges number ", numebr1)
  else:
    if number2 > number3:
      st.write("Largest number ", number2)
    else:
      st.write("Largest number", number3)
    
