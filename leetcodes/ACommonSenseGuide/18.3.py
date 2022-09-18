
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
    pass
                
print(dijkstra_Algo(atlanta, el_paso))    
            
