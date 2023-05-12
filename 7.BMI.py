height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


x=weight/(height**2)
print(x)
y=round(x)
if y<18.5:
    print(f'Your BMI is {y}, you are underweight.')
elif y<25:
    print(f'Your BMI is {y}, you have a normal weight.')
elif y<30:
    print(f'Your BMI is {y}, you are slightly overweight.')
elif y<35:
    print(f'Your BMI is {y}, you are obese.')
else:
    print(f'Your BMI is {y}, you are clinically obese.')