"""! @brief Defines the sensor classes."""

##
# @file sensors.py
#
# @brief Defines the sensor classes.
#
# @section description_sensors Description
# Defines the base and end user classes for various sensors.
# - Sensor (base class)
# - TempSensor
#
# @section libraries_sensors Libraries/Modules
# - random standard library (https://docs.python.org/3/library/random.html)
#   - Access to randint function.
#
# @section notes_sensors Notes
# - Comments are Doxygen compatible.
#
# @section todo_sensors TODO
# - None.
#
# @section author_sensors Author(s)
# - Created by John Woolsey on 05/27/2020.
# - Modified by John Woolsey on 06/11/2020.
#
# Copyright (c) 2020 Woolsey Workshop.  All rights reserved.


import random


class Sensor:
    """! The sensor base class.

    Defines the base class utilized by all sensors.
    """

    def __init__(self, name):
        """! The Sensor base class initializer.

        @param name  The name of the sensor.

        @return  An instance of the Sensor class initialized with the specified name.
        """

        ## The name of the sensor.
        self.name = name
        ## The value of the sensor.
        self.value = random.randint(0, 50)

    def __str__(self):
        """! Retrieves the sensor's description.

        @return  A description of the sensor.
        """

        return f"The {self.name} sensor has a value of {self.value}."


class TempSensor(Sensor):
    """! The temperature sensor class.

    Provides access to the connected temperature sensor.

    Supported units are "F" (Fahrenheit), "C" (Celsius), and "K" (Kelvin)
    with "F" being the default unit.
    """

    def __init__(self, name, unit="F"):
        """! The TempSensor class initializer.

        @param name  The name of the temperature sensor.
        @param unit  The unit of the temperature sensor, defaults to "F".

        @return  An instance of the TempSensor class initialized with the specified name and unit.
        """

        super().__init__(name)
        ## The temperature unit.
        self.unit = unit

    def __str__(self):
        """! Retrieves the temperature sensor's description.

        @return  A description of the temperature sensor.
        """

        return (
            f"The {self.name} temperature sensor has a value of "
            f"{self.value} degrees {self.unit}."
        )

    def set_unit(self, unit):
        """! Sets the temperature unit.

        @param unit  The temperature unit ("F", "C", or "K"),
            defaults to "F" if a valid unit is not provided.
        """

        if unit in ("C", "K"):
            self.unit = unit
        else:
            self.unit = "F"
