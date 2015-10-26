import writing


choice = input ('Enter "1" to generate DB, enter "2" to work with DB ')

if choice == '1':
    print ('Here is new generated DB also written in file "moves" ')
    writing.writing_data()
if choice == '2':
    writing.rewriting_data()




