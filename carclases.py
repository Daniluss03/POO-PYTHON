class Car():
    """ A simple attempt to represent a car"""
    def __init__(self,make,model,year): 
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+''+self.make+''+self.model
        return long_name.title()
    def read_odemeter(self):
        """print a statement showing the cars mileage"""
        print("this car has "+str(self.odometer_reading)+" miles on it")
    def update_odometer(self,mileage):
        """set the odometer reading to the given value"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer!")
    def increment_odemeter(self,miles):
        """add the given amount to  the odometer reading"""       
        self.odometer_reading+=miles

        

my_new_car=Car('audi','a4',2016)
my_new_car.odometer_reading=45
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(2300)
print(my_new_car.read_odemeter())


my_used_car=Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odemeter()
my_used_car.increment_odemeter(100)
my_used_car.read_odemeter()
