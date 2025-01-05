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



