from decorators import ride_logger
from exceptions import InvalidRatingError, RideHistoryFileError, InvalidDistanceError, InvalidVehicleError
from vehicles import Bike, Car, Vehicle

@ride_logger
def book_ride(vehicle):
    
    fare = vehicle.fare_calculation()

    ride_info = (
        f"Driver: {vehicle.rider_name}\n"
        f"Vehicle: {vehicle.__class__.__name__}\n"
        f"Distance: {vehicle.distance} km\n"
        f"Fare: Rs.{fare}\n"
        f"Rating: {vehicle.rating}\n")

    try:
        with open("ride_history.txt", "a") as file:
            file.write(ride_info + "-" * 30 + "\n")
    except RideHistoryFileError as e:
        print(f"Error writing to ride history file {e}")

    return fare

def main():
    try:
        v_type = input("Enter Vehicle Type: ").strip().capitalize()
        rider_name = input("Enter Rider Name: ").strip().capitalize()
        rating = float(input("Enter Rating (1-5): "))
        distance = float(input("Enter Distance (in km): "))

        if distance <= 0:
            raise InvalidDistanceError("Distance must be greater than zero.")

        if v_type =="Car":
            vehicle = Car(rider_name, rating, distance)
        elif v_type == "Bike":
            vehicle = Bike(rider_name, rating, distance)
        else:
            raise InvalidVehicleError(f"Invalid vehicle type: {v_type}. Please enter 'Bike' or 'Car'." )
            return

        fare = book_ride(vehicle)

        print("\nRide Details:")
        print(f"Driver: {vehicle.rider_name}")
        print(f"Vehicle: {vehicle.__class__.__name__}")
        print(f"Distance: {vehicle.distance} km")
        print(f"Fare: Rs.{fare}")

    except (InvalidRatingError, InvalidDistanceError, InvalidVehicleError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
