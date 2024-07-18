import streamlit as st
import pandas as pd
import plotly.express as px

st.title("5教科の点数のレーダーチャート")

A=st.number_input("国語")
B=st.number_input("数学")
C=st.number_input("理科")
D=st.number_input("社会")
E=st.number_input("英語")

df=pd.DataFrame({
    "教科":["国語","数学","理科","社会","英語"],
    "点数":[A,B,C,D,E]
})
fig=px.bar(df,x="教科",y="点数")

st.plotly_chart(fig)