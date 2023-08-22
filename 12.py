a=int(input("enter Year: "))
print(type(a))

if(a % 4 == 0) :
    print("-- leap year --")
else :
    print("-- not leap year --")
         
#or a%100!=0 or a%400 ==0