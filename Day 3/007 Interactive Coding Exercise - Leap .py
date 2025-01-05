#007 Interactive Coding Exercise - Leap year
'''
Logical Error??
'''
year = int(input("Enter a year to see if a year is a leap year or not. "))

if year % 4 == 0:
    if year % 100 == 0 :
        if year % 400 ==  0:
            print("Leap!")
        else:
            print("No.")
    else:
        print("Leap!")
else:
    print("No.")

