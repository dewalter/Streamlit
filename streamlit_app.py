import streamlit as st
import pandas as pd
import numpy as np

st.sidebar('sidebar')

st.title('My First Streamlit App')
st.text ('Hello everybody, my first text field in streamlit')

col1, col2 = st.columns(2)
col1.write('# This is Column 1')
col2.write('# This is Column 2')
