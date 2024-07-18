import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

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

values=([A,B,C,D,E])
labels = [f"データ{i}" for i in range(1, len(values)+1)]
# 多角形を閉じるためにデータの最後に最初の値を追加する。
radar_values = np.concatenate([values, [values[0]]])
# プロットする角度を生成する。
angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)

fig = plt.figure(facecolor="w")
# 極座標でaxを作成。
ax = fig.add_subplot(1, 1, 1, polar=True)
# レーダーチャートの線を引く
ax.plot(angles, radar_values)
#　レーダーチャートの内側を塗りつぶす
ax.fill(angles, radar_values, alpha=0.2)
# 項目ラベルの表示
ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)

ax.set_title("レーダーチャート", pad=20)
plt.show()
st.pyplot.chart(fig)