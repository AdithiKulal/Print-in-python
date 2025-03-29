def hotel_cost(nights): 
    return 120*nights

def plane_ride_cost(city):
    if city == "New York":
        return 250
    elif city == "Chicago":
        return 200
    elif city == "San Francisco":
        return 300
    elif city == "Miami":
        return 280

def rental_car_cost(days):
    if days >= 7:
        return 40*days - 50
    elif days >= 3:
        return 40*days - 20
    else:
        return 40*days

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of car rental: ", rental_car_cost(5))
print("Cost of plane ride: ", plane_ride_cost("San Francisco"))
print("Cost of hotel room: ", hotel_cost(3))
print("Total cost of the trip:", trip_cost("Chicago", 4, 800))
print(trip_cost("Miami", 5, 1000))