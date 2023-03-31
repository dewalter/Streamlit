import streamlit as st
import pandas as pd
import numpy as np

st.balloons()st.progress(10)with st.spinner('Wait for it...'):    time.sleep(10)

st.title('My First Streamlit App')
st.text ('Hello everybody, my first text field in streamlit')

col1, col2 = st.columns(2)
col1.write('# This is Column 1')
col2.write('# This is Column 2')
