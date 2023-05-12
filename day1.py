print('Day 1 - Python Print Function ')
print('\nThe function is declared like this:')
print("\nprint('what to print')")
'''for 3rd statement use double quotes not single quotes to prevent syntax error as print('what to print') has single quotes'''
print('print("what to print")')
'''or do this'''
'''
print('print('what to print')')
above statement dosent work as both have single quotes '''

print('h')
''' 
print('h')
 IndentationError: unexpected indent - if print or any other funtion (like this multi line comment triple quotes too) has a space before it '''

# string concatenation+ nesting of print and input function:

print('hello'+" "+input('your name:'))

# to get length of string use len(string1) or to get length in bytes
# import sys
# sys.getsizeof(string2)

print( len(input('name?')))
import sys
print(sys.getsizeof(input('name?')))

#to switch values
# think theres 2 cups of coffee and juice and you have to swap it how would you do it irl?
# ideally you'd do it with a third cup
# thrid cup would be another variable
'''  code:
x=a 
a=b 
b=x  '''