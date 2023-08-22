# Arithmetic Operators
# Comparison operators
# Logical operators
# Assignment operators
# Membership Operators
# Identity Operators

#1
x = int(input('enter the value of x:'))
y = int(input('enter the value of y:'))
# addition
print('Sum: ', x + y)
# subtraction
print('Subtraction: ', x - y)
# multiplication
print('Multiplication: ', x * y)
# division
print('Division: ', x / y)
# floor division
print('Floor Division: ', x // y)
# modulo
print('Modulo: ', x % y)
# x to the power y
print('Power: ', x ** y)

#2
#a = 20
#b = 17
# equal to operator
print('x == y ', x == y)
# not equal to operator
print('x != y ', x != y)
# greater than operator
print('x > y ', x > y)
# less than operator
print('x < y ', x < y)
# greater than or equal to operator
print('x >= y ', x >= y)
# less than or equal to operator
print('x <= y ', x <= y)

#4
#a = 10
# assign 20 to n2
#b = 20
# assign the sum of n1 and n2 to n1
x += y # n1 = n1 + n2
print("x+=y", x)
x*=y
print('x*=y',x)
x-=y
print('x-=y',x)
x/=y
print('x/=y',x)

#3
#logical operator
#AND,OR,NOT OPERATOR
z=30
#and
if x>y and x>z:
    print('x is largest number')
if y>x and y>z:
    print('y is largest number')
if z>x and z>y:
    print('z is largest number')
#not    
if (not(x>y)):
    print('y is greter')
else:
    print('x is greter')
#or 
ch=(input('enter a charecter:'))
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print(ch,'is a vowel')
else:
    print(ch,'is a constant')
    
#5
#membership operator
mylist=[10,10.5,'mitesh']
n1=10
n2=100
print('10 in mylist')
print('10.5 in mylist')
print('100 i not mylist')
