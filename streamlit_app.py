import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import io
import japanize_matplotlib

# Title of the Streamlit app
st.title("5教科の点数のレーダーチャート")

# Input fields for scores
A = st.number_input("国語", value=0)
B = st.number_input("数学", value=0)
C = st.number_input("理科", value=0)
D = st.number_input("社会", value=0)
E = st.number_input("英語", value=0)

# Create a DataFrame for the bar chart
df = pd.DataFrame({
    "教科": ["国語", "数学", "理科", "社会", "英語"],
    "点数": [A, B, C, D, E]
})

# Create the bar chart using Plotly
bar_fig = px.bar(df, x="教科", y="点数", title="各教科の点数")
if st.button("棒グラフを表示"):
    st.plotly_chart(bar_fig)

# Data for the radar chart
label_list = ['国語', '数学', '理科', '社会', '英語']
acc_list = [A, B, C, D, E] 
acc_list += acc_list[:1]  # Close the radar chart loop

# Calculate angles for radar chart
angle_list = [n / float(len(label_list)) * 2 * np.pi for n in range(len(label_list))]
angle_list += angle_list[:1]

# Create radar chart with Matplotlib
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
plt.xticks(angle_list[:-1], label_list, color='grey', size=12)

# Plot data on radar chart
ax.plot(angle_list, acc_list, linewidth=1, linestyle='solid', label='点数')
ax.fill(angle_list, acc_list, 'blue', alpha=0.25)

# Set chart title and legend
ax.set_title('レーダーチャート', size=20, color='blue', y=1.1)
plt.legend(loc='upper right')

# Save the radar chart to a BytesIO object and display it in Streamlit
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
st.image(buf, caption='レーダーチャート', use_column_width=True)

# Optionally close the plot to prevent display issues
plt.close(fig)
