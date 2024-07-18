import streamlit as st
import pandas as pd
import numpy as np

st.title("5教科の点数のレーダーチャート")

A=st.text_input("国語")
B=st.text_input("数学")
C=st.text_input("理科")
D=st.text_input("社会")
E=st.text_input("英語")
dataframe=(A,B,C,D,E)
columns = ('col %d' % i
    for i in range(5))
dataframe
st.write('This is a line_chart.')
st.line_chart(dataframe)