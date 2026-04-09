# ===================================================================
# NOC GPS Monitoring Configuration - ECTS Style
# ===================================================================
# National Oil Ethiopia (NOC) Electronic Cargo Tracking System
# Main Fuels Depot: Dukem (strategic hub)
# Focus: Fuel tankers, valve monitoring, route compliance, fuel theft prevention
# ===================================================================

VEHICLES = [
    {"vehicle_id": "NOC-T001", "type": "Fuel Tanker", "capacity_liters": 40000, "owner": "NOC"},
    {"vehicle_id": "NOC-T002", "type": "Fuel Tanker", "capacity_liters": 35000, "owner": "NOC"},
    {"vehicle_id": "NOC-T003", "type": "Fuel Tanker", "capacity_liters": 40000, "owner": "NOC"},
    {"vehicle_id": "SUB-T101", "type": "Fuel Tanker", "capacity_liters": 42000, "owner": "Subcontracted"},
    {"vehicle_id": "SUB-T102", "type": "Fuel Tanker", "capacity_liters": 38000, "owner": "Subcontracted"},
    {"vehicle_id": "NOC-V501", "type": "Support Vehicle", "capacity_liters": 0, "owner": "NOC"},
]

# Strategic NOC Delivery Routes (Dukem Depot as origin)
ROUTES = {
    "Dukem_to_Bahir_Dar": {
        "start": (8.8087, 38.9146),
        "end": (11.5936, 37.3908),
        "waypoints": [(8.8087, 38.9146), (9.0, 38.7), (9.8, 38.1), (10.5, 37.8), (11.5936, 37.3908)],
        "distance_km": 520,
        "typical_duration_hours": 12
    },
    "Dukem_to_Dire_Dawa": {
        "start": (8.8087, 38.9146),
        "end": (9.5931, 41.8661),
        "waypoints": [(8.8087, 38.9146), (9.0, 39.2), (9.4, 40.8), (9.5931, 41.8661)],
        "distance_km": 380,
        "typical_duration_hours": 10
    },
    "Dukem_to_Mekelle": {
        "start": (8.8087, 38.9146),
        "end": (13.4969, 39.4707),
        "waypoints": [(8.8087, 38.9146), (9.5, 39.0), (11.0, 39.3), (12.5, 39.4), (13.4969, 39.4707)],
        "distance_km": 780,
        "typical_duration_hours": 18
    },
    "Dukem_to_Hawassa": {
        "start": (8.8087, 38.9146),
        "end": (7.0621, 38.4728),
        "waypoints": [(8.8087, 38.9146), (8.4, 38.7), (7.8, 38.5), (7.0621, 38.4728)],
        "distance_km": 280,
        "typical_duration_hours": 7
    },
    "Dukem_to_Jimma": {
        "start": (8.8087, 38.9146),
        "end": (7.6739, 36.8358),
        "waypoints": [(8.8087, 38.9146), (8.4, 38.0), (7.9, 37.5), (7.6739, 36.8358)],
        "distance_km": 345,
        "typical_duration_hours": 9
    },
    "Dukem_to_Adama": {
        "start": (8.8087, 38.9146),
        "end": (8.5465, 39.2687),
        "waypoints": [(8.8087, 38.9146), (8.7, 39.1), (8.5465, 39.2687)],
        "distance_km": 95,
        "typical_duration_hours": 3
    }
}

# Simulation Parameters
NUM_DAYS = 5
SAMPLES_PER_HOUR = 12          # Every 5 minutes (industry standard GPS ping rate)
START_DATE = "2025-04-01 06:00:00"