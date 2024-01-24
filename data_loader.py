# data_loader.py

import pandas as pd

def load_data():
    demand_points = pd.read_csv("demand_points.csv")
    supply_points = pd.read_csv("supply_points.csv")
    logistics_routes = pd.read_csv("logistics_routes.csv")
    logistics_routes_list = logistics_routes.to_dict('records')
    return demand_points, supply_points, logistics_routes_list
