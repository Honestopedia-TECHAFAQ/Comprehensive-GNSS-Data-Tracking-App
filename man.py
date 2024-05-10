import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import time

def main():
    st.title("GNSS Data Collection App")
    with st.sidebar:
        st.header("Options")
        mode = st.selectbox("Mode", ["Real-time", "Interval"])
        if mode == "Interval":
            interval = st.slider("Interval (seconds)", min_value=1, max_value=60, value=10)
        accuracy = st.slider("Accuracy", min_value=1, max_value=10, value=5)
        action = st.selectbox("Action", ["Fetch Single Point", "Track Series of Points"])

    st.subheader("Data Collection")
    if st.button("Start Data Collection"):
        st.write("Data collection started...")

        if mode == "Real-time":
            while True:
                data = {
                    "Latitude": [37.7749],
                    "Longitude": [-122.4194],
                    "Timestamp": [time.strftime('%Y-%m-%d %H:%M:%S')],
                    "Altitude": [10]
                }
                df = pd.DataFrame(data)
                st.write(df)
                time.sleep(interval)
        
        elif mode == "Interval":
            for i in range(3):
                data = {
                    "Latitude": [37.7749],
                    "Longitude": [-122.4194],
                    "Timestamp": [time.strftime('%Y-%m-%d %H:%M:%S')],
                    "Altitude": [10]
                }
                df = pd.DataFrame(data)
                st.write(df)
                time.sleep(interval)
        if st.button("Export Data to CSV"):
            df.to_csv("gnss_data.csv", index=False)
            st.success("Data exported successfully.")
    st.subheader("Map Visualization")
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)
    folium.Marker([37.7749, -122.4194], popup='GNSS Point').add_to(m)
    folium_static(m)
if __name__ == "__main__":
    main()
