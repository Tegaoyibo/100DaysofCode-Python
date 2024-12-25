#1st input: enter height in meters
height = float(input("What is your height in meters?"))
#2nd input: enter weight in kilograms
weight = float(input("What is your weight in kilograms?"))

BMI = weight/(height**2)
result = str(BMI)
print("Your BMI is: "+ result)