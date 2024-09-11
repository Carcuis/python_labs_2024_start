import streamlit as st
import requests
import pandas as pd
import json

# 获取天气数据
def get_weather_data():
    result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')
    return result.json()

# 主函数
def main():
    st.title("香港天气信息")

    # 获取数据
    data = get_weather_data()

    # 提取温度数据
    temperature_data = data["temperature"]["data"]
    df = pd.DataFrame(temperature_data)

    # 显示所有位置的温度条形图
    st.subheader("各位置温度")
    st.bar_chart(df.set_index('place')['value'])

    # 在侧边栏中添加选择框
    location = st.sidebar.selectbox("选择位置", df['place'])

    # 显示所选位置的温度
    selected_temp = df[df['place'] == location]['value'].values[0]
    st.sidebar.write(f"{location} 的温度是 {selected_temp}°C")

if __name__ == "__main__":
    main()