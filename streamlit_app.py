import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#read in the file
movies_data = pd.read_csv("https://raw.githubusercontent.com/danielgrijalva/movie-stats/7c6a562377ab5c91bb80c405be50a0494ae8e582/movies.csv")

st.title('My First Streamlit App')
st.text ('Hello everybody, my first text field in streamlit')

col1, col2 = st.columns(2)
col1.write('# This is Column 1')
col2.write('# This is Column 2')

movies_data.info()
