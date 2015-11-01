import writing
import sys



'''if choice == '1':
    print ('Here is new generated DB also written in file "moves" ')
    writing.writing_data()
if choice == '2':
    writing.rewriting_data()'''
def ext():
    sys.exit(0)

ch = {
    '1':writing.writing_data,
    '2':writing.rewriting_data,
    '3':ext
    }
def choose():
    choice = input ('Enter "1" to generate DB, enter "2" to work with DB, enter "3" to exit ')
    ch[choice]()
    choose()
choose()
    


