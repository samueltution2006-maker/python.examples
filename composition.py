#composition
class Engine:
    def __init__(self, horsepower):
        print("Engine constructor called")
        self.horsepower = horsepower    #120

    def start(self):
        return "Engine started."

class Car:
    def __init__(self, make, model, horsepower):    #make - Toyota, model - Corolla, horsepower - 120
        self.make = make     # Toyota
        self.model = model   # Corolla
        # Composition: A Car has an Engine object as an attribute
        # engineObj = Engine()
        self.engine = Engine(horsepower)   #120

    def drive(self):
        # Accessing functionality of the composed object
        engine_status = self.engine.start()
        return f"{self.make} {self.model} is driving. {engine_status}"

# Create a Car object 
# Creating an object for the class will invoke the __init__ method automatically
my_car = Car("Toyota", "Corolla", 120)

# Use the Car object's methods, which in turn use the Engine's methods
print(my_car.drive())

myEngine = Engine(180)
myEngine.start()