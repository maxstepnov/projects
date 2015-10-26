import data_enter as de
import math
import pickle



def writing_data():
    f = open ('moves.txt','wb')
    pickle.dump(de.fill_db(),f)
    f.close()

def open_data():

    try:
        f = open ('moves.txt', 'rb')
        s = pickle.load(f)
        f.close()
        return s
    except EOFError:
        writing_data()

def rewriting_data():

    db = dict(open_data())
    print (db)
    lst = list(db.items())
    for i in lst:
        print (
            'Car '+str(i)+ ' moved '+ str(math.sqrt((i[1][0][0])*2+(i[1][0][1]))*2)+' km')
    

    car = (input ('Enter sign of a car to move it ')).upper()
    x,y = de.new_xy()
    for i in lst:
        if x == i[1][0][0] and y == i[1][0][1]:
            print ('No chance! This coordinates are used.')
            de.new_xy()
        
        

    if car in db:
        db[car]=([(x, y), db[car][1], db[car][2]])
        print ('DB with changes:')
        print (db)
        
        f = open ('moves.txt','wb')
        pickle.dump(db,f)
        f.close()
    
    else:
        print ('No such car sign in DBase')
    

rewriting_data()

