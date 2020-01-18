# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    def __init__(self):
        # Base class

    class FlightVehicle(Vehicle):
        def __init__(self):
            super().__init__()
            self.mode = mode

        class Starship(FlightVehicle):
            def __init__(self):
                super().__init__()
                self.space_bound = True

        class Airplane(FlightVehicle):
            def __init__(self):
                super().__init__()

    class GroundVehicle(Vehicle):
        def __init__(self):
            super().__init__()
            self.mode = "ground"
            self.wheels = wheels

        class Car(GroundVehicle):
            def __init__(self):
                super().__init__(, wheels)

        class Motorcycle(GroundVehicle):
            def __init__(self):
                super().__init__(, wheels)
