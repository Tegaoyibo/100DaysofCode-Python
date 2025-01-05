
'''
#You have to import the random module first.

#import random
#random_int = random.randint(100,200) returns a random integer between a and b (inclusive)
#random_float = random.random() from [0,1) non inclusive of 1

#code
import random
random_float = random.random()*5 #takes no arguments
print(random_float)
# multiplying by the desired (non-inclusive)range 
'''
import random
random_int = random.randint(0, 1)

if random_int == 0:
    print("Heads")
else:
    print("Tails")
