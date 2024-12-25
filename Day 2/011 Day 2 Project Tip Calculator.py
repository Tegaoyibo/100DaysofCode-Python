#011 Day 2 Project Tip Calculator.mp4
print("Welcome to the tip calculator!")
flat_price = float(input("What was the total bill? $"))
grat_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))/100
people =int(input("How many people to split the bill? "))

tip = (flat_price*grat_amount)
total = tip+flat_price
split = round(total/people, 2)

#f string not necessary. Just practicing!
print(f"Each person should pay: ${split}")