# Author: SMR (AMDG) 12/15/21

# Import Random to get random number generation
import random

# Define the Function
def clone():

# Inputting either Y or N
    orig = input("Name a clone? ")

# Converting if lower to upper    
    orig = orig.upper()

# Creating Whitespace list to save later    
    name_list = []
    
    for x in range(9999):

# Need to append b/c range(9999) truly means 9998        
        name_list.append(x + 1)
    list = []
    while orig == "Y":
        name = random.choice(name_list)
        name_list.remove(name)
        name = str(name)

# Length Conditionals in order to figure out the 0's
        if len(name) == 3:
            fin_name = "CT-0" + name
        elif len(name) == 2:
            fin_name = "CT-00" + name
        elif len(name) == 1:
            fin_name = "CT-000" + name
        else:
            fin_name = "CT-"+ name
        print("New clone trooper name: {0}".format(fin_name))
        list.append(fin_name)

# Need Unless it will run on forever
        orig = input("Name a clone?")
        orig = orig.upper()

# Print the Final List with Names
    print(list)

# Final Call of function
clone()