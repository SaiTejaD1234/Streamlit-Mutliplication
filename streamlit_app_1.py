import streamlit as st
import pandas as pd
import numpy as np

st.title('Mutliplication of 2 Numbers')
a = st.number_input('Enter the first number')
st.write('The first number is ', a)

b = st.number_input('Enter the second number')
st.write('The second number is ', b)

c=a*b

if(st.button(' Calculate Product')):
    st.subheader('The product of the two numbers is {}'.format(c))

