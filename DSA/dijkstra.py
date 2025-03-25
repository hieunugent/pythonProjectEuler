class City:
    def __init__(self, name):
        self.name = name 
        self.routes = {}
    def add_routes(self, city, price):
        self.routes[city] = price

