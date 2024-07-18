import streamlit as st
import pandas as pd
import plotly.express as px
st.title("5教科の点数のレーダーチャート")

A=st.text_number("国語")
B=st.text_number("数学")
C=st.text_number("理科")
D=st.text_number("社会")
E=st.text_number("英語")

df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=[A,B,C,D,E]))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.show()