
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
    cheapest_price_table= {}
    cheapest_previous_stop_over = {}
    unvisited_city = []
    visited_cities ={}
    cheapest_price_table[starting_city.name] = 0
    current_city = starting_city
    while current_city:
        visited_cities[current_city.name]= True
<<<<<<< HEAD
        if unvisited_city:
            print("There is a Unvisited City")
            unvisited_city.remove(current_city.name)
        value = current_city.route.keys()
       
        for v in value:
            print(v.name)
            
            
        break

=======
        print(visited_cities)
        if unvisited_city:
            
            
               
>>>>>>> 9d84df1ba0d4e9f0a871874dd062a0f175a638fe
print(dijkstra_Algo(atlanta, el_paso))    
            
