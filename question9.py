total_spots = 5 
available_spots = list(range(total_spots))  
stack = []  # Stack for parked cars
queue = []  # Queue for waiting cars
def park_car(car_id):
    if available_spots: 
        spot = available_spots.pop()  
        stack.append((car_id, spot)) 
        print(f"Car {car_id} parked in spot {spot}.")
    else:
        queue.append(car_id)  
        print(f"Car {car_id} is waiting to park.")

# Function to remove a car
def remove_car(car_id):
    for i, (parked_car_id, spot) in enumerate(stack):
        if parked_car_id == car_id:
            stack.pop(i) 
            available_spots.append(spot)  
            print(f"Car {car_id} removed from spot {spot}.")
            if queue:
                waiting_car = queue.pop(0)  
                park_car(waiting_car) 
            return
    print(f"Car {car_id} not found.")

# Example usage
park_car('A')  # Park car A
park_car('B')  # Park car B
park_car('C')  # Park car C
park_car('D')  # Park car D
park_car('E')  # Park car E
park_car('F')  # Car F should wait

remove_car('B')  # Remove car B
remove_car('C')  # Remove car C