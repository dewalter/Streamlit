import streamlit as st
import pandas as pd
import numpy as np

st.container()

st.title('My First Streamlit App')
st.text ('Hello everybody, my first text field in streamlit')

col1, col2 = st.columns(2)
col1.write('# This is Column 1')
col2.write('# This is Column 2')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
