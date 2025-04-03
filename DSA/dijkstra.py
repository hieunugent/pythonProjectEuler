class City:
    def __init__(self, name):
        self.name = name 
        self.routes = {}
    def add_routes(self, city, price):
        self.routes[city] = price
# declare the  city
london = City("London")
berlin = City('Berlin')
newyork =City('NewYork')
chelse =City("Chelse")
chicago =City("Chicago")
sandiego =City("San Diego")
# declare the routes possible for each city
london.add_routes(berlin.name,120)
london.add_routes(newyork.name, 300)
london.add_routes(chelse.name, 320)
berlin.add_routes(newyork.name, 200)
berlin.add_routes(chicago.name,100)
berlin.add_routes(sandiego.name,400)
newyork.add_routes(chelse.name,1000)
newyork.add_routes(chicago.name, 10)
chelse.add_routes(chicago.name,500)
chelse.add_routes(sandiego.name, 600)
chicago.add_routes(sandiego.name, 210)
# print(berlin.name)
# print(london.routes)
# print(berlin.routes)







def dijkstra_func(starting_city,destination_city):
    cheapest_price_table={}
    cheapest_previous_stopover_table={}
    unvisited_city=[]
    visited_city={}
    cheapest_price_table[starting_city.name]=0
    current_city = starting_city
    print(current_city.name)
    while current_city:
        visited_city[current_city.name] = True
        if current_city in unvisited_city:
            unvisited_city.remove(current_city)
        for adjacent_city in current_city.routes:
            if adjacent_city not in visited_city:
                unvisited_city.append(adjacent_city)
        current_city = min(unvisited_city, key=lambda city : cheapest_price_table[city.name])





    return 0
    # while current_city:
    #     visited_city[current_city.name]=True
    #     if current_city in unvisited_city:
    #         unvisited_city.remove(current_city)
    #     for adjacent_city,price in current_city.routes.items():
    #         if adjacent_city not in visited_city:
    #             unvisited_city.append(adjacent_city)
    #         price_through_current_city = cheapest_price_table[current_city.name] + price
    #         if not cheapest_price_table[current_city.name] or price_through_current_city < cheapest_price_table[current_city.name]:
    #             cheapest_price_table[current_city.name] = price_through_current_city
    #             cheapest_previous_stopover_table[adjacent_city.name] = current_city.name
    #     current_city = min(unvisited_city, key=lambda city : cheapest_price_table[city.name])

    # # shortest_path =[]
    # current_city_name = destination_city.name
    # while current_city_name != starting_city.name:
    #     shortest_path.append(current_city_name)
    #     current_city_name = cheapest_previous_stopover_table[current_city_name]
    # shortest_path.append(starting_city.name)

    # return shortest_path.reverse()



print(dijkstra_func(london,sandiego))