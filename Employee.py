class Employee:
    def __init__(self, name=None, age=None, salary=None):
        self.name = name
        self.age = age
        self.salary = salary

    #Creates an __str__ method that allows an object created from this class to be passed to the print function
    def __str__(self):
        return "This is an Employee class"

    #Creates a getter and setter methods for the name attribute for encapsulation
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name