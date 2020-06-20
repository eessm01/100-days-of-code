"""A set of classes used to represent gas and electrical cars."""

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attibutes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print('This car has {} miles on it.'.format(
            str(self.odometer_reading)
        ))

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attemots to rol the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print('This car has {}-KWh battery'.format(
            self.battery_size
        ))

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car go aproximately {}'.format(range)
        message += ' miles on a full charge.'
        print(message)


class ElectricCar(Car):
    """Represent aspects of a car, specific to electrical vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize atttributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        #super(ElectricCar, self).__init__(make, model, year)  #python2.7
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()

    # def describe_battery(self):
    #     """Print a statement describing the battery size."""
    #     print("This car has a {}-KWh battery.".format(
    #         self.battery_size
    #     ))

    def fill_gas_tank(self):
        """Electric cars don't have a gas tanks."""
        print('This car doesn\'t need a gas tank!')
 

