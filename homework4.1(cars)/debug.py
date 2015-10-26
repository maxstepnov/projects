#coding: utf-8
import carsdatabase
import ainmodule



#funcs.get(actn)


wdata = carsdatabase.opening()

#searching car by name or its part

def namesearch():

    global carslist

    # searching by full name
    carName = input ("Enter car's name or its PART to find its horse power rate: ")
    carslist = list(wdata.items())

    if carName in wdata:
        print (carName + 'has '+ str(wdata[carName]) + 'horse powers')

    # searching by part of a name
    for y,i in carslist:
        if carName in y:
            print (str(y) + ' has ' + str(i) + ' horse powers')
    hpsearch()

    #searching car's horse power rate:
def hpsearch():

    global carPower
    carPower = int(input ("Enter car's hp rate: "))

    for y,i in carslist:
        if carPower == i:
            print (str(y) + ' has ' + str(i) + ' horse power rate')

    sort()
    #list sorting
def sort():

    carslist.sort( key = lambda x: x[0])
    s1 = carslist
    print ("List sorted by the car's name: ")
    for i in range(len(s1)):
            
        print (str(carslist[i]))

    rangesearch()



#searching cars with hp in a range:

def rangesearch():
    rangemin = int (input('Enter min of range '))
    rangemax = int (input('Enter max of range '))

    cnt = 0
    ranged = []
    for x,y in carslist:
        if rangemin <= y <= rangemax:
             ranged.append(carslist[cnt])       
        cnt +=1
    print ('These cars are in range of '+ str(rangemin)+ ' and ' + str(rangemax) + ' horse powers ')
    for i in ranged:
         print(i)


def choice():

    actn = input ('Enter "1" to enter data,  "2" to search data, "3" to delete or change data, "4" to exit ')    


    if actn == '1':
        ainmodule.data_entering()
        choice()
    elif actn == '2':
        namesearch()
        choice()
    elif actn == '3':
        carsdatabase.delelem()
        choice()
    elif actn == '4':
        pass
    else:
        choice()
            
choice()


