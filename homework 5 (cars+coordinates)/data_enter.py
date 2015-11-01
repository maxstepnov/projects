#это из нового заданя. Все генерируется рандомом: номер тачки, координаты
#рандомно выбирается имя из списка и прочее
import random
        
#sign generation (генерируется европейский(!) номер)
def generate_sign():
    
    signhex = ''
    for i in range(3):
       
        sign = str(hex(random.randint(8,17)))
        #sign = int(random.randint(10,36), base=26)
        
        signhex += sign[2:].upper()
    
    return signhex

#coordinates gen
def generate_xy():
    
    xpoint = random.randint(0,100)
    ypoint = random.randint(0,100)
    
    #print (xpoint, ypoint)
    return xpoint, ypoint

#name
def generate_name():
    car_list = ['Mazda','Lexus', 'Infiniti', 'Opel', 'Volkswagen', 'BMW', 'Mercedes',
                'Subaru', 'Nissan', 'Toyota', 'Suzuki', 'Mitsubishi', 'Honda']
    car_name = car_list[random.randint(0,len(car_list)-1)]
    return car_name

# horse power rate
def generate_hp():
    carhp = random.randint(90, 350)
    return carhp

# all together now goes to database 'd'
def fill_db():
    d = {}
    for i in range(random.randint(10,15)):
        d[generate_sign()] = [generate_xy(), generate_name(), generate_hp()]
    carlist = list(d.items())
    for i in range(len(carlist)):
        print (carlist[i])    
    return carlist

def new_xy():
    try:
        x = int(input('Enter new X '))
        y = int(input('Enter new Y '))

    except ValueError:
        print ('Should be number!')
        x = int(input('Enter new X '))
        y = int(input('Enter new Y '))
    
    return x,y

   
    
