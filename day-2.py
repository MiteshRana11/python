#DATA TYPE
#they are defined int,float,comlex;functions are type(),isinstance()
#a.numers
n1=10
print(n1,"is of type",type(n1))
n2=10.5
print(n2,"is of type",type(n2))
print(n2,"is complex number?",isinstance(10.5,int))
n3=1+2j
print(n3,"is complex number?",isinstance(1+2j,complex))

#string
#string are defined single qutetion and double qutetion
name="mitesh"
#prints complate string
print("name is:",name)
#prints first character of the string 
print(name[0])
#prints string starting from 3rd to 5th character
print(name[2:5])
#prints string starting from to 3rd character
print(name[2:])
#prints string two times
print(name*2)
#prints concatenated string
print(name+"hello")

#list data type
list1=[10,20,30,"mitesh",40,50,"rana",60]
print("list1[2]=",list1[2])
print("list1[3:5]=",list1[3:5])
print("list1[5:]=",list1[5:])
print("list1[0:5]=",list1[0:5])

#creating an empty list
lst=[]
n=int(input("enter number of elements:"))
for i in range(0,3):
    ele=input("enter value:")
    lst.append(ele) #adding the element
    print(lst)

#tuple data type symbol = (()) user can't change the value;list symbol = ([]) user can change the sine.

tuple=(10,"mitesh",20,30,40,"rana")
print("tuple[0:2]=",tuple[0:2])
print("tuple[3:]=",tuple[3:])

#d={1:'mitesh',2:'rana','key':3}
#print(type(d))
m1={}
n=int(input('enter number of ele:'))
for i in range(0,n):
    a,b=input('enter key value pair data:').split()
    m1[a]=b
print(m1)

#sum of variable
name=(input("enter name:"))
print(name)
n1=int(input("enter num:"))
n2=int(input("enter num2:"))
ans=n1+n2
print("sum is",ans)

#conditional statement
#if Statement 
#if...else Statement 
#if...elif...else Statement
#match-case Statement
#Nested if statements
#Ternary Operator
#1
n1 = int(input("enter num:"))
if n1 % 2 == 0:
    print("Number is even")
if n1 % 2 == 1:
    print("Number is odd")

#2
n1 = int(input("enter num:"))
if n1 % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#3
#if condition:
#Statements to be executed
#elif condition:
#Statements to be executed
#elif condition:
#Statements to be executed
#lse:
#Statements to be executed
n1 = 11
if n1 == 10:
   print("n1 is 10")
elif n1 > 10:
    print("n1 is greater than 10")
else:
    print("n1 is less than 10")
#4
#match variable:
#case matching_value_1: statement_1
#case matching_value_2: statement_2
#case matching_value_3: statement_3
ch = int(input("Enter value:"))
match ch:
    case 1:
        print("This is one")
    case 2:
        print("This is two")
    case 3:
        print("This is three")
    case _:
        print("Invalid value")

