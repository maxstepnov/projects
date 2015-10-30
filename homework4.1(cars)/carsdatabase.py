
# coding: utf-8

import pickle
import ainmodule 

data = {}
dbase = {}

#renovating database with entered data
def refresh_data():
    def renew():
        #data updating from module 'ainmodule'
        ainmodule.data_entering()
        ss = ainmodule.data
        print(ss)
        data.update(ss)
        
        global dbase
        f = open ('dbase.txt', 'rb')

        try:
            dbase = pickle.load(f)
        except EOFError:
            dbase = data

        dbase.update(data)
        f.close()
        print (dbase)
    renew()


    #data writing

    def writing():
        f = open ('dbase.txt', 'wb')

        pickle.dump(dbase,f)

        f.close()
    writing ()

    #opening DB for work

def opening():
    f = open ('dbase.txt', 'rb')

    dbase = pickle.load(f)

    f.close()
    return dbase



def delelem():
    dlt = input('Enter a name to delete it or change: ')
    f = open ('dbase.txt', 'rb')
    dbase = pickle.load(f)
    if dlt in dbase:
        cd = input ('Press "c" to change element or "d" to delete it: ')
        if cd == 'd':
            print ('Element '+ str(dlt)+': '+ str(dbase.pop(dlt))+ ' deleted!')
        if cd == 'c':
            def tryint():
                try:
                    nw = int(input ('Enter new value for ' + dlt + ' '))
                    dbase[dlt] = nw
                    print(dbase[dlt])
                    print ('New value for '+ str(dlt) + ' is '+str(dbase[dlt]))
                except UnboundLocalError:
                    print ('Should be integer!!!')
                    tryint()
                f = open ('dbase.txt', 'wb')
                pickle.dump(dbase, f)
                print (dbase)
                f.close()

            tryint()
    else:
        print ('No such key in database')
        
            
    f = open ('dbase.txt', 'wb')
    pickle.dump(dbase, f)
    f.close()


    




