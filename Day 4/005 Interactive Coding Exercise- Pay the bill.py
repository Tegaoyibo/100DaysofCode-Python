'''
- Documentation on list and methods.
- List is an ordered data structure.
- Items in the string can have different data types
- # Example of list: my_list = [item1, item2]
    - Comma separated values inside a square brackets
- Can use indexing to locate an item in a list
    - Can use negative number for indexing. List acesses from reverse.
- To add/append an item to the end of the list:
    - example: states_of_america.append("Angelaland")
- To extend a list with a list of items you can use the extend 
    - example: list.extend(["item31","item32","item33"])
'''
#Select a random item from list
import random

names_string = str(input("Enter the names of the people to see who will pay:\n"))
names = names_string.split(", ") #splits a string into list
number = len(names)


random_item = random.randint(0,number-1)

print(names[random_item])
