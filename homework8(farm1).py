#conding: utf-8

import random
import time

#randomizing weather that influences the amount of the product
def weather():
    wlist = ['storm','rain','clouds','sunny']
    wstate = random.randint(0,3)
    if wstate == 0:
        product_rate = 0
    elif wstate == 3:
        product_rate = 2
    else:
        product_rate = 1

    return product_rate

#how an animal feels itself (ill or healhy, if healthy - no products)

def health():
        ill = False
        health_rate = random.randint(1,10)
        
        if health_rate < 3:
            ill = True
        else:
            ill = False
        return ill
    
#basic class Animal

class Animal():    
    
    name = None
    product = 0

#class cow
class Cow(Animal):
    product_name = 'milk'
    ill = health()
    
    name = 'Burenka'
    def act(self):
        if self.ill == False:
            self.product += 1*weather()
        else:
            self.product = 0
        return self.product

#class hen
class Hen(Animal):

    product_name = 'eggs'
    ill = health()
    name = 'Henny'    

    def act(self):
        if self.ill == False:
            self.product += 1*weather()
        else:
            self.product = 0
        return self.product

#class pig based on Animal
class Pig(Animal):

    product_name = 'meat'
    ill = health()
    name = 'Piggy'

    def act(self):
        if self.ill == False:
            self.product += 1*weather()
        else:
            self.product = 0
        return self.product
    
# creating animals
pig1 = Pig()
hen1 = Hen()
cow1 = Cow()
lst = [pig1, hen1, cow1]

#class farm that produces products and shows results
class Farm:
    amount = 0
    def month(self):
        for i in lst:
            for j in range(period):
                a = i.act()
            print (str(i.name)+' gave '+str(a)+ ' points of '+i.product_name)

#entering period
period = int(input ('Enter period(days) to know how your farm functions '))

#show data
farm = Farm()
farm.month()

time.sleep(10)
