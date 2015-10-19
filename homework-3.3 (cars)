# coding: utf-8
import collections
import pickle
data = {}
ext = ''

#car's name checking
while ext != 'exit':
    
    def car_check():
        global car
        car = input("Enter auto's name: ")
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
    
    
    data[car] = int(hp)
    print (data)
    

    
    ext = input ("Type 'exit' to finish entering or press key to go on ")


#writing entered data

f = open ('dbase.txt', 'rb')
try:
    dbase = pickle.load(f)
except EOFError:
    dbase = data
dbase.update(data)

f.close()

f = open ('dbase.txt', 'wb')

pickle.dump(dbase,f)

f.close()

#opening DB for work

f = open ('dbase.txt', 'rb')

dbase = pickle.load(f)

#searching car by name or its part

carName = input ("Enter car's name or its PART to find its horse power rate: ")
carslist = list(dbase.items())


if carName in dbase:
    print (carName + 'has '+ str(dbase[carName] + 'horse powers'))

for y,i in carslist:
    if carName in y:
        print (str(y) + ' has ' + str(i) + ' horse powers')

#searching car's horse power rate:

carPower = int(input ("Enter car's hp rate: "))

for y,i in carslist:
    if carPower == i:
        print (str(y) + ' has ' + str(i) + ' horse power rate')

#searching cars with hp in a range:
        
rangemin = int (input('Enter min of range '))
rangemax = int(input('Enter max of range '))

carslist.sort( key = lambda x: x[1])
s1 = carslist
ranged=[]
cnt = 0
print ("List sorted by the car's name: "+ '\n' + str(carslist))

for x,y in carslist:
     
    if rangemin <= y <= rangemax:
         ranged.append(carslist[cnt])       
    cnt +=1
print ('These cars are in range of '+ str(rangemin)+ ' and ' + str(rangemax) + ' horse powers ' + str(ranged))

f.close()    
