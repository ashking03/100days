#using type conversion every time while using print function is tedious
x = input('enter height')
y = input('enter age')
z = True
print('your height is '+x)
print('your age is '+y)
# print('the info is '+z)
# here, x and y is taken from input function, as we know the input() function returns string values to the program
# however, the last print statement gives a TypeError : can only concatenate str (not 'bool') to str
# to prevent this from happening use an f string
print(f'your info is {z}')
a = 2
b = 7.9
print(f'you are {a} times better than you were {b} months ago ')