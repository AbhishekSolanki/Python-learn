# object Oriented Programming

class vehicle: #super class (Inheritance)
    wheels = 4
    def __init__(self):
        print "Vehicle"
    def calcVelocity(self,x):
        return 3*x+10

class Car(vehicle): #Class Declaration
    def __init__(self): #Default constructor, Self parameter to reference object itself
        self.speed = 10



exampleCar = Car() #Creating a object
print exampleCar.speed #accessing variables by objects
print exampleCar.calcVelocity(20) # calling from super class (Inheritance concept)
print exampleCar.wheels
