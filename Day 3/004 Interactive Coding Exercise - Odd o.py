#004 Interactive Coding Exercise - Odd or Even Introducing Modulo
'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height>120: #have to include the colon after the if and else keyword
    print("You can ride the rollercoaster!") #any lines of code indented after the if/else keyword means that that is a block of code
else:
    print("Sorry. You can not ride the rollercoaster")
'''
#Which number do you want to check?
number = int(input("Enter a number: \n"))
remainder = number%2

if remainder == 0: #You can also write it like if number%2 == 0
    print("This number is even!")
else:
    print("This number is odd!")

