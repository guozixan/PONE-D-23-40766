# logistics_model.py

class LogisticsPoint:
    def __init__(self, point_id, quantity, point_type, location, time_window):
        self.point_id = point_id
        self.quantity = quantity
        self.type = point_type
        self.location = location
        self.time_window = time_window

class LogisticsRoute:
    def __init__(self, route_id, start_point, end_point, duration, cost, risk_level):
        self.route_id = route_id
        self.start_point = start_point
        self.end_point = end_point
        self.duration = duration
        self.cost = cost
        self.risk_level = risk_level
