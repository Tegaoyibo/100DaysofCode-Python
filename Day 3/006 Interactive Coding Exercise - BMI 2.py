#006 Interactive Coding Exercise - BMI 2.0
'''
Lecture Example of COntrol Statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height>=120: #have to include the colon after the if and else keyword
    print("You can ride the rollercoaster!") #any lines of code indented after the if/else keyword means that that is a block of code
    age = int(input("What is your age? "))
    if age < 12: # This only appears if the previous if condition is true
        print("Please pay $5.")
    elif age <=18: #First condition is true, but second (nested) one is not.
        print("Please pay $7.")
    else:
    print("Please pay $12.") #First condition is true, but third (nested) one is not.
else: #if first condition is not true.
    print("Sorry. You can not ride the rollercoaster.")
'''
height = float(input("What is your height in meters?"))
weight = float(input("What is your weight in kilograms?"))

BMI = weight/(height**2)

if BMI < 18.5: 
    print(f"Your BMI is {BMI} and you're underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI} and you're normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI} and you're slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI} and you're overweight.")
else:
    print(f"Your BMI is {BMI} and you're clinically obese.")

'''
Takeaways: 
The way I initially had it:
    if 25 < BMI >= 18.5:
is read as if 15 is less than the BMI and the BMI is greather than or equal to 18.5.

Here is the example code that helped me realize my mistake:

x = 10

if x > 15:
    print("x is greater than 15")
elif x > 10:
    print("x is greater than 10 but less than or equal to 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is less than or equal to 5")

Condition will be read from left to right.
'''



