
try:
    number = int(input("Enter a number: "))         #try this code and if it is not correct use except statement
    print(number)

except:
    ("Invalid Input")

try:    #try this code if it executed correctly then good else except statement will come into play

    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("invalid input")