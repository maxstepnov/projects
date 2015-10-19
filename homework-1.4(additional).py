import math

a = [1,-20,38,0,44,0]
b = [88,-20,48,4,33,2]
winner = []

for i in range(len(a)):
    if a[i] > b[i]:
        print (b[i])
        winner.append(b[i])
    else:
        print (a[i])
        winner.append(a[i])

    if abs(a[i] - b[i]) < 15:
        
        c = abs(a[i] - b[i])
        elemNum = (i + 1 + c)%len(a)
        if a[i] > b[i]:
            print ('Congrats! Element-winner is ' + str(b[elemNum]))
        else:
            print ('Congrats! Element-winner is ' + str(a[elemNum]))
