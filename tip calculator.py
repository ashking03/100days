print('welcome to my tip calculator <3')
b=float(input('enter bill amount: '))
p=int(input('enter number of people: '))
t=float(input('enter tip percentage(no % sign please) : '))
x=t/100
y=x+b
z=y/5
w=round(z,2)
print(f'each person must pay {w} rupees.')