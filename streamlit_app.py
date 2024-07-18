import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib

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

if st.button("棒グラフ"):
    st.plotly_chart(fig)


label_list = ['国語', '数学', '理科', '社会', '英語']
acc_list = [A,B,C,D,E] 
acc_list += acc_list[:1]  

acc_list_2 = [A,B,C,D,E]  
acc_list_2 += acc_list_2[:1]  # チャートを閉じるために最初の値を末尾に追加

# レーダーチャートを描画するためのangle_listを計算
angle_list = [n / float(len(label_list)) * 2 * np.pi for n in range(len(label_list))]
angle_list += angle_list[:1]

# matplotlibでレーダーチャートを描画
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
plt.xticks(angle_list[:-1], label_list, color='grey', size=12)

# # プロット線を描画
ax.plot(angle_list, acc_list, linewidth=1, linestyle='solid', label='Model A')
ax.fill(angle_list, acc_list, 'blue', alpha=0.1)

ax.plot(angle_list, acc_list_2, linewidth=1, linestyle='solid', label='Model B')
ax.fill(angle_list, acc_list_2, 'red', alpha=0.1)


# # チャートを表示
plt.legend(loc='upper right')
plt.show()