
#задаем имена в список
lst = ['Alex First', 'George Second', 'Mike Third', 'Phillip Forth', 'Mike Fifth', 'Alex Sixth']
studID = 1
s1 =[]

#находим имя по индексу

i = int(input('Enter index '))
if i<len(lst):
    print (str(lst[i]))
else: print ('No such value')

#находим имя по срезу

i1 = int(input('Enter first i '))
i2 = int(input('Enter last i '))
print (str(lst[i1:i2]))

#находим всех студентов, в имени которых нашлась "р"

for i in lst:
    
    if i.find('p') >= 0:
        print ('This student has "p" in his name: '+ str(studID) +': '+str(i))
    studID+=1

#поиск студентов с одинаковыми именами

    for y in lst:
        if y[0:3] == i[0:3] and i != y:
            s1.append(y)
s1.sort()
print ('These students have same names: ' + str(s1))

#поиск действий конкретного студента, здесь использовал дополнительный цикл со сплитом для интереса;),
#более правильное решение использовано при поиске действий

s2=[]
f = open('studlog.txt')

for z in f:
    a = z.split(':')
    s2.append(a[0])

 
name = input ("Input student's name: ")
if name in s2:
    s = open('studlog.txt')
    for i in s:
        if i.find(name) != -1:
            print (i)
    s.close()
else:
    print ("Name is not in student's list")

#поиск действий студента
    
action = input ("Enter student's action: ")
s = open ('studlog.txt')
for i in s:
    if i.find(action) != - 1:
        print (i)
s.close()
            
  
