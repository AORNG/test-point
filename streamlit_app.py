import streamlit as st
import folium

def main():
    st.title("Streamlitで地図を表示する")

    # 地図の中心座標を設定
    center = [35.6895, 139.6917]  # 例：東京の緯度経度

    # Foliumのマップオブジェクトを作成
    m = folium.Map(location=center, zoom_start=10)

    # StreamlitでFoliumの地図を表示
    folium_static(m)

if __name__ == "__main__":
    main()