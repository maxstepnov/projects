# coding: utf-8

import carsdatabase
import random

data = {}
dbase = {}
ext = ''

#car's name checking
def data_entering():
    
    def car_check():
        global car
        car = input("Enter auto's name: ").capitalize()
        if car.isalpha() == False:
            print ('Should be used letters only!')
            car_check()
        return car
    car_check()
    
    # horse power rate checking

    def hp_check():
        global hp
        hp = input ("Enter its horse power rate: ")
      
        if hp.isnumeric() == False:
            print ('Should be used digits only!')
            hp_check()

        return hp
    hp_check()

    #creating dictionary and adding items
    
    def datadata(car, hp):
        data[car] = int(hp)
        return data
    datadata(car,hp)
    #carsdatabase.refresh_data()        
    ext = input ("Type 'go' to go on entering data or press 'enter' key to finish ")
    if ext == 'go':
        data_entering()




