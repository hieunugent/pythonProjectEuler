from unicodedata import name


class City:
    def __init__(self, name):
        self.name = name
        self.route = {}
    def add_route(self,city, price):
        self.route[city] = price
    
atlanta = City("Atlanta") 
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago,120)
boston.add_route(denver, 180)
chicago.add_route(el_paso,80)
denver.add_route(chicago, 40)
denver.add_route(el_paso,140)

def dijkstra_Algo(starting_city, final_destination):
    cheapest_price_table = {}
    cheapest_previous_stopover_city_table = {}
    unvisited_cities = []
    visited_cities = {}
    cheapest_price_table[starting_city.name] = 0
    current_city = starting_city
    
    while current_city:
        visited_cities[current_city.name] = True
        unvisited_cities.pop(current_city)
        for adjacent_city, price in enumerate(current_city):
            if visited_cities[adjacent_city.name]:
                unvisited_cities.append(adjacent_city)
            price_through_current_city = cheapest_price_table[current_city.name] +price
            if not cheapest_price_table[current_city.name] or price_through_current_city < cheapest_price_table[adjacent_city.name]:
                cheapest_price_table[adjacent_city.name] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacent_city.name] = current_city.name
        if unvisited_cities:
            current_city = unvisited_cities[0]
            current_price = cheapest_price_table[current_city.name]
        for city in unvisited_cities:
            if cheapest_price_table[city.name] < current_price:
                current_city = city
        
                
    
            
