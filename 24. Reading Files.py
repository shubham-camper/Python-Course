

employee_file = open("employees.txt", "r")

print(employee_file.readable())     #it will tell you if the file is readable or not
print(employee_file.read())     #it will completely read the file
print(employee_file.readline())             #it will the print first line of the file
print(employee_file.readline())         #then it will print out the second line of the file
print(employee_file.readlines())        #it will print out the lines of the file
print(employee_file.readlines()[1])     #it will print out the second element of the file

for employee in employee_file.readlines():          #it will read out lines one by one and print it out
    print(employee)
employee_file.close()