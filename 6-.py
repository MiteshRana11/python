a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number : '))
d = int(input('Enter four number : '))
if a > b and a > c and a > d:
    print("a is the largest number")
if b > a and b > c and b > d:
    print("b is the largest number")
if c > a and c > b and c > d:
    print("c is the largest number")
if d > a and d > b and d > c:
    print("d is the largest number")