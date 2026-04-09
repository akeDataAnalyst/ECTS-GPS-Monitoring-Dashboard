# Real-Time Fleet & Tanker Monitoring Dashboard
[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)](https://ects-gps-monitoring-dashboard-4dsht9vtx3yiyqcencfspb.streamlit.app/)

## ECTS-Style GPS Monitoring & Alert System 

---

## Description
This project a complete real-time GPS monitoring system, modeled after their Electronic Cargo Tracking System (ECTS).

The solution provides end-to-end capabilities for monitoring company-owned and subcontracted fuel tankers, detecting irregularities, and generating actionable insights. It includes four structured phases — from realistic data generation to an interactive Streamlit dashboard — demonstrating full-cycle telematics monitoring.

---

## Problem
National Oil Ethiopia faces critical operational and financial challenges with its fuel distribution fleet:

- **Fuel theft and misuse**: Sudden fuel drops and unauthorized valve opening during deliveries cause significant revenue loss.
- **Route deviations and unauthorized stops**: Lead to delays, increased fuel consumption, and safety risks.
- **Limited visibility**: Difficulty in real-time monitoring of both own and subcontracted tankers.
- **Compliance pressure**: Need to meet Petroleum & Energy Authority requirements for tracking accuracy and reporting.
- **Slow response**: Delayed detection of irregular activities reduces delivery efficiency and increases risk.

---

## Solution
I developed a complete GPS monitoring solution that closely mirrors NOC’s operational environment:

- Generated high-fidelity synthetic telematics data simulating NOC operations from the strategic Dukem Fuels Depot to major delivery routes (Bahir Dar, Dire Dawa, Mekelle, Hawassa, Jimma, Adama).
- Conducted deep Exploratory Data Analysis to understand movement patterns, fuel behavior, valve status, and anomalies.
- Built an intelligent alert system to detect:
  - Fuel Theft Suspect
  - Valve Tampering
  - Prolonged Stops
  - Route Deviations
  - Harsh Driving
- Implemented historical trip replay, root-cause analysis, and JD-aligned KPIs (Tracking Accuracy, On-Time Deliveries, Route Deviation reduction).
- Interactive Dashboard: A clean, professional Streamlit web application with live fleet map, alert dashboard, fuel trends, and trip replay functionality.

The system uses industry-standard columns (odometer, valve_status, ignition_status, harsh events, device_status) and realistic Ethiopian route logic.

---

## Recommendation
I recommend implementing a similar real-time GPS monitoring platform as the core tool in NOC’s GPS Control Center. Key benefits include:

- **Immediate Operational Gains**:
  - Faster detection and response to fuel theft and valve tampering (potential 15–25% reduction in fuel losses)
  - Improved route compliance and on-time delivery performance
  - Enhanced safety through early identification of prolonged stops and harsh driving

- **Strategic Recommendations**:
  - Deploy automated high-severity alerts (Fuel Theft Suspect & Valve Tampering) via SMS/email to operations teams
  - Generate weekly "Deviation Hotspots" and "Fuel Anomaly Reports" for logistics and driver coaching
  - Use the KPI framework for monthly regulatory reporting to the Petroleum & Energy Authority
  - Integrate with existing ECTS devices and coordinate closely with the IT/Telecom team for device maintenance

---

## Tech Stack
- **Core Language**: Python 3
- **Dashboard Framework**: Streamlit
- **Visualization**: Plotly, Folium + Streamlit-Folium
- **Geospatial Analysis**: GeoPy
- **Data Processing**: Pandas, NumPy
---
