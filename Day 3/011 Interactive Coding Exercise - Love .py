#011 Interactive Coding Exercise - Love calculator
#check for the number of times the letters of True occur
#check the number of times the letters of LOVE occur
#concat the numbers together
'''
If score is less than 10 or greater than 90: "You guys go together like Coke and mentos"
If score is between 60 and 50: "You are alright together"
Otherwise: "Your score is x."
'''

print("The Love Calculator is calculating your score...")
name1 = str(input("Enter the name of the first person."))
name2 = str(input("Enter the name of the second person."))

combined = name1+name2
lowered = combined.lower()

t = lowered.count("t")
r = lowered.count("r")
u = lowered.count("u")
e = lowered.count("e")

val1 = t+r+u+e

l = lowered.count("t")
o = lowered.count("t")
v = lowered.count("t")
e = lowered.count("t")

val2 = l+o+v+e

str(val1)
str(val2)

score = val1+val2

if score <10 or score>90:
    print(f"Your score is: {score}. You guys go together like Coke and Mentos!")
elif score <60 or score>50: #elif bc this if statemet is if the previous one is not true. This way, else can be used if nothing else works.
     print(f"Your score is: {score}. You are alright together.")
else:
    print(f"Your score is: {score}.")
