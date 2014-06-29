# object Oriented Programming

class Car: #Class Declaration
    def __init__(self): #Default constructor, Self parameter to reference object itself
        self.speed = 10

    def calcVelocity(self,x):
        return 3*x+10


exampleCar = Car() #Creating a object
print exampleCar.speed #accessing variables by objects
print exampleCar.calcVelocity(20)
