#Object oriented programming is type of data type which is used to store information about particular object

class Student:    #Now we have created the class Student and now we can store information about student in this class

    def __init__(self, name, major, gpa, is_on_probation):          # whatever the information we type in the student class will be stored in this name will be stored in name, major, gpa and is_on_probation or not
        self.name = name            #it will identify the name in the first place major in second place and so on
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

