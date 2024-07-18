import streamlit as st
import pandas as pd
import numpy as np

st.title("5教科の点数のレーダーチャート")

A=st.text_number("国語")
B=st.text_number("数学")
C=st.text_number("理科")
D=st.text_number("社会")
E=st.text_number("英語")
values = np.array([A,B,C,D,E])
labels = [f"データ{i}" for i in range(1, len(values)+1)]