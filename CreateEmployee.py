
import re

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printPersonInfo(self):
        print("Name: ", str(self.name), " " , "Age: ", str(self.age))

class Employee(Person):
    def __init__(self, name, age, email):
        super().__init__(name, age)     #calls the parent constructor
        self.email = email
    
    def printEmployeeInfo(self):
        print("Name: ", str(self.name), " ", "Age: ", str(self.age), " ", "Email: ", str(self.email))

def createEmployee():
    while True:
        name = input("Enter name: ")
        if not re.match("^[a-zA-Z\s]+$", name): #matches: starting with, any letter or whitepace, one or more times, till the end of the line 
            print("Invalid name. Name should contain only letters and spaces.") # otherwise user is given an error and repromted for their name
            continue
        
        age = input("Enter age: ")
        if not re.match("^[0-9]+$",age): #matches: starting with, any number , one or more times
            print("Invalid age. Age should be a positive integer.") # otherwise user is given an error and repromted for their name
            continue
        
        email = input("Enter email: ")
        if not re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email): #match: starts with any letter or number, one or more times, followed by @, any number or letter, one or more times,followed by a ., then any letter, 2 or more times
            print("Invalid email format.")
            continue
        
        return Employee(name, int(age), email)

# Example usage:
new_employee = createEmployee()
new_employee.printEmployeeInfo()