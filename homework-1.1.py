#coding utf-8
import os

# открыли файл, вместо слова "питон" ищем слово "ворд", т.к. в папке не было файлов с "питоном." внутри)))

list=os.listdir('.')
resu = open('result.txt','r+')
search = 'word'
for i in list:
    
    f = open(i,'r')
    
    s = f.read()
    wordcount=s.count(search)
    print(s.count(search))
    
     
    if s.count(search)>0:
        resu.write('number of elements:'+  str(wordcount)+' in file '+ i +'\n')
        #resu.write(i + '\n')
        print(i)
    f.close()
resu.close()
   
