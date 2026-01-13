import random
import json
class Employee:
    def __init__ (self, first,last,employee,salary):
        self.first = first
        self.last = last
        self.number = employee
        self.salary = salary
        self.email = first + '.' + str(employee) + '@ANCompany.com'
    def full_name(self):
        print(f"{self.first} {self.last}")
    def __str__(self):
        return (
            f"Name: {self.first} {self.last}\n"
            f"Employee Number: {self.number}\n"
            f"Salary: {self.salary}\n"
            f"Email: {self.email}"
        )

employee_1 = Employee("awdiden","Lizzer",6019758,24000)

print(employee_1)
        