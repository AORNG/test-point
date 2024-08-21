import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

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
labels = ['国語', '数学', '理科', '社会', '英語']
values = [A, B, C, D, E]
values += values[:1]  # Close the radar chart loop

# Calculate the angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]  # Close the radar chart loop

# Create radar chart with Plotly
radar_fig = go.Figure()

radar_fig.add_trace(go.Scatterpolar(
    r=values,
    theta=labels,
    fill='toself',
    name='点数',
    line=dict(color='blue')
))

radar_fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]  # Adjust the range based on your data
        )
    ),
    showlegend=True,
    title='レーダーチャート'
)
if st.button("レーダーチャートを表示"):
# Display the radar chart
    st.plotly_chart(radar_fig)
