#in this file we will create a module call useful_tools
#and import it in the 26. Modules and Pip file
#so all these function we created can be used there

import random       #random module does random things these are all modules

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon ", "Paul MacCatney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):     #roll_dice will roll the dice from 1 till the num you have selected
    return random.randint(1, num)
