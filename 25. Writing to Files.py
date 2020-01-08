

employee_file = open("employees.txt", "a")      #it will append a element in the file
employee_file.write("\nToby - Human Resources")
employee_file.write("\nKelly - Customer Service")

employee_file = open("employees.txt", "w")          #it will write rewrite all the element of the file
employee_file.write("\n Kelly Customer Service")

employee_file = open("employees1.txt", "w")      #it make new file employees

employee_file.write("\nKelly - Customer Service ")

employee_file = open("index.html", "w")     #you can also write html file with it
employee_file.write("<p>This is HTML</p>")          #and put elements inside it

employee_file.close()