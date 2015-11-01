#conding: utf - 8
import random

#creating class Tank

class Tank:
    def __init__(self, speed = None):
        
        self.shassi = 2
        self.gus = True
        self.model = 'T-34'
        if speed:
            self.speed = speed
        else:
            self.speed = 120
    def status(self):
        if self.gus == True:
            self.status = 'Driving'
        print(self.model + ' is ' +self.status+ '(chassis detected)')
#creating class Car
            
class Car:
    gus = False
    modellst = ['Lada', 'BMW', 'Lexus', 'ZAZ', 'Opel']
    
    speed = 190
        
    def status(self):
        #random choice for model and wheels amount
        self.model = self.modellst[random.randint(0,4)]
        self.wheels = random.randint(3,4)

        if self.wheels < 4:
            self.status = 'Broken'
        elif self.model == 'Lada' or 'ZAZ':
            self.status = 'Slowly Driving'
        else:
            self.status = 'Fast Driving'
            

        print(self.model + ' is ' +self.status+ '(' + str(self.wheels) + ' wheels detected)')
#creating class Carriage

class Carriage:
        
    wheels = random.randint(3,4)
    gus = False
    speed = 20
    model = 'Carriage'
    def status(self):
        #random choice for wheels amount
        if self.wheels < 4:
            self.status = 'Broken'
        else:
            self.status = 'Slowly driving'
        print(self.model + ' is ' +self.status+ '(' + str(self.wheels) + ' wheels detected)')

#objects car1, car2 are created
car1 = Car()
car2 = Car()
#obj tank is created

tank = Tank(speed = '100')
# obj carraige is created

carriage = Carriage()
lst = [car1, car2, tank, carriage]

#status checking
for i in range(len(lst)):
    lst[i].status()
    

