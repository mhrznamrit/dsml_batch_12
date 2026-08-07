from abc import ABC, abstractmethod
from exceptions import InvalidRatingError, InvalidDistanceError

class Vehicle(ABC):
    def __init__(self, rider_name, rating, distance):
        self.rider_name = rider_name
        self.rating = rating
        self.distance = distance

    @abstractmethod
    def fare_calculation(self):
        pass

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if 1 <= value <= 5:
            self.__rating = value
        else:
            raise InvalidRatingError("Rating must be between 1 and 5")


class Car(Vehicle):
    base_fare = 50
    rate = 25
   
    def fare_calculation(self):
        if self.distance <= 0:
            raise InvalidDistanceError("Distance must be greater than zero.")
        return self.base_fare + (self.distance * self.rate)


class Bike(Vehicle):
    base_fare = 20
    rate = 10
  
    def fare_calculation(self):
        if self.distance <= 0:
            raise InvalidDistanceError("Distance must be greater than zero.")
        return self.base_fare + (self.distance * self.rate)