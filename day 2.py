"""
data types -> int , float, str, boolean
type() function is used to find type of data
use print(type(variable))
"""
# x=len(input('name?\n'))
# print('your name has '+x+'characters.\n')
"""
name?
saanvi

TypeError: can only concatenate str (not "int") to str
here type error as x is an int type 
Traceback (most recent call last):
 
    print('your name has '+x+'characters.\n')
to prevent this use TYPE CONVERSION: 
y=str(x) : this converts any data type to string
y=float(x) : converts any type to string
"""

x = len(input('name?\n'))
y = str(x)
print('your name has ' + y + ' characters.\n')

"""
hierarchy of operators : PEMDAS
paranthesis, exponential , divison , multiplication , addition , subtraction
input() function returns a string data type to program . Convert it into int/float to do math operations
ex: BMI CALCULATOR"""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
x=float(weight)
y=float(height)
z=y*y
res = x/z
print(int(res))

#round off numbers to int or float by using round() function
print(round(2.666668,2))
#this rounds 2.666668 to 2 decimal places
print(round(3.6))
#this just rounds off the number to an int data type

#divison always produces a float . Ex: 4/2 gives 2.0
#to get an int as a result use // instaed of /

print(4/2)
print(4//2)
print(type(4//2))