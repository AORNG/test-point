import streamlit as st
import pandas as pd
import plotly.express as px

st.title("5教科の点数のレーダーチャート")

A=st.text_number("国語")
B=st.text_number("数学")
C=st.text_number("理科")
D=st.text_number("社会")
E=st.text_number("英語")

df=pd.DataFrame({
    "教科":["国語","数学","理科","社会","英語"],
    "点数":[A,B,C,D,E]
})
fig=px.bar(df,x="教科",y="点数")

st.plotly_chart(fig)