# ==============================================================
# REVERSE ENGINEERING OF AN AI-BASED NAVIGATION SYSTEM
# System: Google Maps - AI-Based Navigation & Route Planning
# ==============================================================

import heapq
import random
from collections import defaultdict

# ==============================================================
# 1. SYSTEM DECOMPOSITION & ANALYSIS
# ==============================================================

class GPSLocationModule:
    """Determines current location and destination."""

    def get_location(self):
        return "A"

    def get_destination(self):
        return "F"


class MapDataModule:
    """Stores road-network and geographical information."""

    def __init__(self):
        self.graph = {
            "A": [("B", 4), ("C", 2)],
            "B": [("A", 4), ("C", 1), ("D", 5)],
            "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
            "D": [("B", 5), ("C", 8), ("E", 2), ("F", 6)],
            "E": [("C", 10), ("D", 2), ("F", 3)],
            "F": [("D", 6), ("E", 3)]
        }

    def get_graph(self):
        return self.graph


class TrafficAnalysisModule:
    """Analyzes traffic conditions."""

    def __init__(self):
        self.traffic = {
            ("A", "B"): 1.2,
            ("A", "C"): 1.0,
            ("B", "C"): 1.1,
            ("B", "D"): 1.5,
            ("C", "D"): 1.8,
            ("C", "E"): 1.2,
            ("D", "E"): 1.0,
            ("D", "F"): 1.6,
            ("E", "F"): 1.0
        }

    def get_traffic_factor(self, source, destination):
        return self.traffic.get(
            (source, destination),
            self.traffic.get((destination, source), 1.0)
        )


class RoutePlanningModule:
    """Calculates the best route."""

    def __init__(self, graph, traffic_module):
        self.graph = graph
        self.traffic_module = traffic_module

    def calculate_cost(self, source, destination, distance):
        traffic_factor = self.traffic_module.get_traffic_factor(
            source, destination
        )
        return distance * traffic_factor

    def find_route(self, start, goal):
        priority_queue = [(0, start, [start])]
        visited = set()

        while priority_queue:
            cost, current, path = heapq.heappop(priority_queue)

            if current in visited:
                continue

            visited.add(current)

            if current == goal:
                return path, cost

            for neighbor, distance in self.graph[current]:
                if neighbor not in visited:
                    new_cost = cost + self.calculate_cost(
                        current,
                        neighbor,
                        distance
                    )
                    heapq.heappush(
                        priority_queue,
                        (new_cost, neighbor, path + [neighbor])
                    )

        return None, float("inf")


class NavigationUI:
    """Displays route, ETA and navigation information."""

    def display(self, route, cost):
        print("\n========== NAVIGATION OUTPUT ==========")
        print("Recommended Route :", " -> ".join(route))
        print("Estimated Cost    :", round(cost, 2))
        print("Navigation Status : Route calculated")
        print("=======================================")


# ==============================================================
# 2. ARCHITECTURE RECONSTRUCTION
# ==============================================================

def architecture_reconstruction():
    print("\n\n========== ARCHITECTURE RECONSTRUCTION ==========")

    architecture = [
        "User",
        "GPS & Location Module",
        "Map Data Module",
        "Traffic Analysis Module",
        "AI / ML Processing Layer",
        "Route Planning Module",
        "Navigation & User Interface"
    ]

    for i, component in enumerate(architecture):
        if i < len(architecture) - 1:
            print(f"{component} --> {architecture[i + 1]}")
        else:
            print(component)

    print("\nArchitecture Layers:")
    print("1. Data Collection Layer")
    print("2. Data Processing Layer")
    print("3. AI / ML Layer")
    print("4. Route Optimization Layer")
    print("5. Application / Navigation Layer")


# ==============================================================
# 3. ALGORITHM IDENTIFICATION
# ==============================================================

def traffic_prediction(historical_data):
    """
    Simplified traffic prediction using average historical traffic.
    This is an educational approximation.
    """

    if not historical_data:
        return 1.0

    prediction = sum(historical_data) / len(historical_data)

    return round(prediction, 2)


def eta_prediction(distance, speed):
    """Regression-style simplified ETA calculation."""

    if speed <= 0:
        return None

    eta_hours = distance / speed
    eta_minutes = eta_hours * 60

    return round(eta_minutes, 2)


def pattern_recognition(traffic_values):
    """Identifies whether traffic is increasing."""

    if len(traffic_values) < 2:
        return "Insufficient Data"

    average = sum(traffic_values) / len(traffic_values)

    if average > 1.5:
        return "Heavy Traffic"
    elif average > 1.2:
        return "Moderate Traffic"
    else:
        return "Light Traffic"


def algorithm_identification():
    print("\n\n========== ALGORITHM IDENTIFICATION ==========")

    historical_traffic = [1.1, 1.3, 1.4, 1.5, 1.6]

    predicted_traffic = traffic_prediction(historical_traffic)

    print("Historical Traffic :", historical_traffic)
    print("Predicted Traffic  :", predicted_traffic)
    print(
        "Traffic Pattern    :",
        pattern_recognition(historical_traffic)
    )

    distance = 20
    speed = 40

    eta = eta_prediction(distance, speed)

    print("Distance           :", distance, "km")
    print("Average Speed      :", speed, "km/h")
    print("Predicted ETA      :", eta, "minutes")

    print("\nInferred Algorithms:")
    print("- Graph-based route optimization")
    print("- A* / shortest-path style search")
    print("- Machine learning for traffic prediction")
    print("- Regression-style ETA prediction")
    print("- Pattern recognition")
    print("- Dynamic re-routing")


# ==============================================================
# 4. DATA FLOW & PROCESS MAPPING
# ==============================================================

def data_flow():
    print("\n\n========== DATA FLOW & PROCESS MAPPING ==========")

    data_sources = {
        "GPS Data": "Current user location",
        "User Input": "Destination and travel preference",
        "Map Data": "Roads, distances and locations",
        "Traffic Data": "Current congestion",
        "Historical Data": "Previous traffic patterns"
    }

    print("\nINPUT DATA SOURCES")

    for source, description in data_sources.items():
        print(f"{source:<18} -> {description}")

    print("\nPROCESSING PIPELINE")
    print("1. Data Collection")
    print("       ↓")
    print("2. Data Cleaning")
    print("       ↓")
    print("3. Data Integration")
    print("       ↓")
    print("4. Map Matching")
    print("       ↓")
    print("5. AI / ML Analysis")
    print("       ↓")
    print("6. Route Planning")
    print("       ↓")
    print("7. ETA Prediction")
    print("       ↓")
    print("8. Navigation Output")
    print("       ↓")
    print("9. Continuous Updating")


# ==============================================================
# 5. IMPROVEMENT & REDESIGN
# ==============================================================

def redesigned_system():
    print("\n\n========== IMPROVEMENT & REDESIGN ==========")

    limitations = [
        "Dependence on internet and GPS connectivity",
        "Incorrect predictions due to poor-quality data",
        "High computational requirements",
        "Delay during sudden traffic incidents",
        "Privacy and security concerns"
    ]

    print("\nExisting Limitations:")
    for i, limitation in enumerate(limitations, 1):
        print(f"{i}. {limitation}")

    improvements = [
        "Distributed cloud architecture",
        "Real-time stream processing",
        "Caching of frequently requested routes",
        "Independent modular services",
        "Data validation and preprocessing",
        "Parallel route calculations",
        "Efficient graph-search algorithms",
        "Dynamic resource allocation"
    ]

    print("\nProposed Improvements:")
    for i, improvement in enumerate(improvements, 1):
        print(f"{i}. {improvement}")

    print("\nRedesigned Architecture:")
    print("Data Sources")
    print("     ↓")
    print("Real-Time Data Streaming")
    print("     ↓")
    print("Distributed Processing")
    print("     ↓")
    print("AI / ML Traffic Prediction")
    print("     ↓")
    print("Map & Graph Processing")
    print("     ↓")
    print("Route Optimization")
    print("     ↓")
    print("Dynamic Re-routing")
    print("     ↓")
    print("Navigation Interface")


# ==============================================================
# 6. DYNAMIC RE-ROUTING
# ==============================================================

def dynamic_rerouting(route_module, start, destination):
    print("\n\n========== DYNAMIC RE-ROUTING ==========")

    route1, cost1 = route_module.find_route(start, destination)

    print("Initial Route :", " -> ".join(route1))
    print("Initial Cost  :", round(cost1, 2))

    # Simulate sudden traffic increase
    route_module.traffic_module.traffic[("A", "C")] = 3.0
    route_module.traffic_module.traffic[("D", "F")] = 2.5

    route2, cost2 = route_module.find_route(start, destination)

    print("\nTraffic conditions changed!")
    print("Updated Route :", " -> ".join(route2))
    print("Updated Cost  :", round(cost2, 2))

    if route1 != route2:
        print("Decision      : Alternative route selected")
    else:
        print("Decision      : Existing route retained")


# ==============================================================
# 7. MAIN SYSTEM EXECUTION
# ==============================================================

def main():

    print("=" * 60)
    print(" AI-BASED NAVIGATION SYSTEM")
    print(" Reverse Engineering Demonstration")
    print("=" * 60)

    # Create modules
    gps = GPSLocationModule()
    map_module = MapDataModule()
    traffic = TrafficAnalysisModule()

    route_module = RoutePlanningModule(
        map_module.get_graph(),
        traffic
    )

    navigation = NavigationUI()

    # ----------------------------------------------------------
    # SYSTEM DECOMPOSITION
    # ----------------------------------------------------------

    start = gps.get_location()
    destination = gps.get_destination()

    print("\n========== SYSTEM DECOMPOSITION ==========")
    print("Current Location :", start)
    print("Destination      :", destination)

    print("\nMajor Modules:")
    print("1. GPS & Location Module")
    print("2. Map Data Module")
    print("3. Traffic Analysis Module")
    print("4. Route Planning Module")
    print("5. Navigation & User Interface Module")

    # ----------------------------------------------------------
    # ROUTE PLANNING
    # ----------------------------------------------------------

    route, cost = route_module.find_route(
        start,
        destination
    )

    if route:
        navigation.display(route, cost)
    else:
        print("No route found.")

    # ----------------------------------------------------------
    # ARCHITECTURE
    # ----------------------------------------------------------

    architecture_reconstruction()

    # ----------------------------------------------------------
    # ALGORITHMS
    # ----------------------------------------------------------

    algorithm_identification()

    # ----------------------------------------------------------
    # DATA FLOW
    # ----------------------------------------------------------

    data_flow()

    # ----------------------------------------------------------
    # IMPROVEMENT
    # ----------------------------------------------------------

    redesigned_system()

    # ----------------------------------------------------------
    # DYNAMIC RE-ROUTING
    # ----------------------------------------------------------

    dynamic_rerouting(
        route_module,
        start,
        destination
    )

    # ----------------------------------------------------------
    # FINAL RESULT
    # ----------------------------------------------------------

    print("\n\n========== FINAL RESULT ==========")
    print("System Analysis       : Completed")
    print("Architecture Analysis : Completed")
    print("Algorithm Analysis    : Completed")
    print("Data Flow Mapping     : Completed")
    print("System Redesign       : Completed")
    print("Dynamic Re-routing    : Demonstrated")
    print("==================================")


# ==============================================================
# PROGRAM START
# ==============================================================

if __name__ == "__main__":
    main()
