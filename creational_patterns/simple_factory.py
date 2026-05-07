class Car:
    def drive(self):
        return "Driving Car"

class Bike:
    def drive(self):
        return "Riding Bike"

class VehicleFactory:
    @staticmethod
    def create_vehicle(type):
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            raise ValueError("Invalid vehicle type")
