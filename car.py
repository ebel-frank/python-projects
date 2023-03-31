# this is our superclass
class Car(object):
    """This is the class docstring."""

    def __init__(self, year, make, model):
        self.year = str(year)
        self.make = make
        self.model = model
        self.static = "constant car data"

    def __str__(self):
        """Formats a nice string."""
        return 'String representation: %s %s %s' % (self.year, self.make, self.model)

    def print_car(self):
        '''Echoes back the full name of the vehicles.'''
        print('{0} {1} {2}'.format(self.year, self.make, self.model))
        print(self.static)  # just to show of an attribute fetch


if __name__ == '__main__':
    ns = Car('2010', 'Toyota', 'Camery')
    ns.print_car()

'''
#This is our subclass; inherits from Car
class Motorcycle(Car):
    pass

hs = Motorcycle("1900", "Nissan", "Sentra")
print(hs)
hs.static = 'constant MC data'
print(hs.static)
hs.printcar()
'''
