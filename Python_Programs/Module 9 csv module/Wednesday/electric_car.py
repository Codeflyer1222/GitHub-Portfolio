#!/usr/bin/env python3
#
# Problem: Example of class composition
# Files:
#     electric_car.py - this file is from the author's examples; it is used in C9
# 
# Author: matthes
# Matthes, E. (2022). Python crash course. O’Reilly Media. 
# Date: NA
#

# the following is added to the author's original to show class composition
class Engine:
    def start (self):
        print ("Engine started")

class Wheel:
    def rotate (self):
        print ("Wheel rotating.")
# Finish addition

# define Car class
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.engine = Engine () # added - car has an engine
        self.wheels = [Wheel() for _ in range (4)] #added - car has 4 wheels

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    # the following is added to the author's code
    def drive (self):
        self.engine.start()
        for wheel in self.wheels:
            wheel.rotate()
        print (f"{self.make} {self.model} is driving.")

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

#DON'T USE UNDERSCORES FOR CLASSES. ITS JUST PROPER.
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
  
# create an instance of an Electric car
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# print the car information
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.drive ()