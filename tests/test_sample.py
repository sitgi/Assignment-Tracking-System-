
from creational_patterns.simple_factory import VehicleFactory

def test_vehicle_factory():
    car = VehicleFactory.create_vehicle("car")
    assert car.drive() == "Driving Car"
