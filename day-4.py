#while loop
i=1
while i<=5:
    print('i is:',i)
    i+=2#i=i+2
else:
   print('invalid data')

#range(start,stop,step size)    
for i in reversed(range(5)):
    print('first range:',i)
for i in range(0,3):
    print('first range:',i)
for i in range(5,0,-1):
    print('first range:',i)
else:
    print('****no value left****')

mydata = [10, 20.5,'mitesh','rana',"Hello"]
for i in range(len(mydata)):
    print("Value is ",mydata[i])

for i in range(5):
    if i==3:
        continue#break
    print('value is:',i)

for x in range(10):
    pass#(statement)
    if x % 2 == 0:
        continue
    print('value is:',x)