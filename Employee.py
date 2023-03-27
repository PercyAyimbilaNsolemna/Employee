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

    #Creates a getter and setter methods for the age attribute for encapsulation
    def getAge(self):
        return._age

    def setAge(self, age):
        self._age = age


def main():
    employee = Employee()
    print(employee)

    employee.setName("Percy")
    print(f"Name: {employee.getName()}")

if __name__ == "__main__":
    main()