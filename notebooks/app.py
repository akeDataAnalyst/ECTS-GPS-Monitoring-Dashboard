import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="NOC ECTS Control Center", layout="wide", page_icon="🚛")

# Professional styling
st.markdown("""
    <style>
    .big-font {font-size: 28px !important; font-weight: bold; color: #1E3A8A;}
    .metric-card {background-color: #f8f9fa; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
    </style>
""", unsafe_allow_html=True)

st.title("NOC ECTS Telematics Control Center")
st.markdown("**Real-Time GPS Monitoring Dashboard** ")

# Path setup
import sys
from pathlib import Path
project_root = Path.cwd().parent if "notebooks" in str(Path.cwd()) else Path.cwd()
sys.path.append(str(project_root))

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('../data/processed/noc_telematics_with_alerts_final.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
selected_vehicle = st.sidebar.selectbox("Vehicle", ["All"] + sorted(df['vehicle_id'].unique()))
selected_severity = st.sidebar.multiselect("Alert Severity", ["High", "Medium", "Low"], default=["High"])
selected_alerts = st.sidebar.multiselect("Alert Type", 
                                        options=sorted(df['alert_type'].unique()), 
                                        default=["Fuel Theft Suspect", "Valve Tampering", "Prolonged Stop"])

# Date range
min_date = df['timestamp'].min().date()
max_date = df['timestamp'].max().date()
date_range = st.sidebar.date_input("Date Range", [min_date, max_date])

# Apply filters
filtered = df.copy()
if selected_vehicle != "All":
    filtered = filtered[filtered['vehicle_id'] == selected_vehicle]
if selected_severity:
    filtered = filtered[filtered['alert_severity'].isin(selected_severity)]
if selected_alerts:
    filtered = filtered[filtered['alert_type'].isin(selected_alerts)]
if date_range and len(date_range) == 2:
    filtered = filtered[(filtered['timestamp'].dt.date >= date_range[0]) & 
                        (filtered['timestamp'].dt.date <= date_range[1])]

# KPI Cards
st.subheader("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Tracking Accuracy", "93.66%", delta="↑")
with col2:
    st.metric("On-Time Deliveries", "100.0%")
with col3:
    st.metric("Fuel Theft Alerts", str(df['fuel_drop_alert'].sum()), "🔴")
with col4:
    st.metric("High Severity Alerts", str((filtered['alert_severity'] == 'High').sum()))

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["Dashboard Overview", "Live Fleet Map", "Active Alerts", "Analytics"])

with tab1:
    st.subheader("Dashboard Overview")
    col_a, col_b = st.columns(2)
    with col_a:
        fig = px.pie(filtered, names='alert_type', title="Alert Distribution")
        st.plotly_chart(fig, use_container_width=True)
    with col_b:
        fig2 = px.bar(filtered['vehicle_id'].value_counts().head(8), title="Alerts per Vehicle")
        st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("Live Fleet Map")
    
    # Get latest position per vehicle
    latest = filtered.groupby('vehicle_id').last().reset_index()
    
    # Create clean map
    m = folium.Map(location=[9.0, 38.8], zoom_start=7, tiles="CartoDB positron")
    
    for _, row in latest.iterrows():
        # Color coding based on severity
        if row['alert_severity'] == 'High':
            color = "red"
            icon_color = "red"
        elif row['alert_severity'] == 'Medium':
            color = "orange"
            icon_color = "orange"
        else:
            color = "blue"
            icon_color = "blue"
        
        # Clean and professional popup
        popup_html = f"""
        <div style="font-family: Arial; min-width: 200px;">
            <b style="color:{color};">{row['vehicle_id']}</b><br>
            <b>Alert:</b> {row['alert_type']}<br>
            <b>Severity:</b> <span style="color:{color};">{row['alert_severity']}</span><br>
            <b>Speed:</b> {row['speed_kmh']} km/h<br>
            <b>Time:</b> {row['timestamp'].strftime('%Y-%m-%d %H:%M')}
        </div>
        """
        
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=folium.Popup(popup_html, max_width=300),
            icon=folium.Icon(color=icon_color, icon="truck", prefix="fa")
        ).add_to(m)
    
    st_folium(m, width=950, height=580)

with tab3:
    st.subheader("Active Alerts")
    alerts = filtered[filtered['alert_type'] != 'Normal'].sort_values('timestamp', ascending=False)
    if not alerts.empty:
        st.dataframe(alerts[['timestamp', 'vehicle_id', 'alert_type', 'alert_severity', 
                            'speed_kmh', 'stop_duration_minutes', 'valve_status']], 
                    use_container_width=True, height=500)
    else:
        st.success("No active alerts in the current filter.")

with tab4:
    st.subheader("Analytics & Trends")
    fuel_df = filtered[filtered['fuel_level_percent'].notna()]
    fig = px.line(fuel_df, x='timestamp', y='fuel_level_percent', color='vehicle_id', 
                  title="Fuel Level Trends Over Time")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Trip Replay")
    vehicle = st.selectbox("Select Vehicle", options=sorted(df['vehicle_id'].unique()))
    trips = df[df['vehicle_id'] == vehicle]['trip_id'].unique()
    trip_choice = st.selectbox("Select Trip", options=trips)
    
    if st.button("Show Trip Details"):
        trip_data = df[(df['vehicle_id'] == vehicle) & (df['trip_id'] == trip_choice)]
        st.write(f"**Route:** {trip_data['route'].iloc[0]}")
        alerts_in_trip = trip_data[trip_data['alert_type'] != 'Normal']
        if not alerts_in_trip.empty:
            st.dataframe(alerts_in_trip[['timestamp', 'alert_type', 'alert_severity']])
        else:
            st.info("No alerts in this trip.")

st.caption("**Developed by Aklilu Abera Dana** | **GPS Monitoring Officer** | **ECTS Simulation** | **Supply Chain Data Analyst** | **2026**")