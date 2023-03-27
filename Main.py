from Employee import Employee

def main():
    employee = Employee()
    print(employee)

    employee.setName("Percy")
    print(f"Name: {employee.getName()}")

    employee.setAge(12)
    print(f"Age: {employee.getAge()}")

    employee.setSalary(200000)
    print(f"Salary: ${employee.getSalary()}")

if __name__ == "__main__":
    main()