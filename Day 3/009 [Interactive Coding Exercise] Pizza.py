009 [Interactive Coding Exercise] Pizza Order Practice
'''
Small pizza = $15
Medium pizza = $20
Large pizza = $25
Extra pepperoni (S) = +$2
Extra pepperoni (M, L) = +$3
Extra cheeze (any size)= +$5

'''
S = 15
M = 20
L = 25

print("Thank you for choosing Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want Pepperoni Pizza? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

if size == "S":
    if add_pepperoni == "Y":
        S += 2
    else:
        S
    if extra_cheese == "Y":
        S += 5
        print(f"Total price: {S}")
    else:
        S
        print(f"Total price: {S}")
elif size == "M":
    if add_pepperoni == "Y":
        M += 3
    else:
        M
    if extra_cheese == "Y":
        M += 5
        print(f"Total price: {M}")
    else:
        M
        print(f"Total price: {M}")
else:
    if add_pepperoni == "Y":
        L += 3
    else:
        L
    if extra_cheese == "Y":
        L += 5
        print(f"Total price: {L}")
    else:
        L
        print(f"Total price: {L}")
'''
Takeaways:
Print statement only necessary for final if/else condition!
'''

