# realistic_example.py

# Base class
class Employee:
    def __init__(self, name, age, salary):
        """Initialize the Employee object with name, age, and salary."""
        self.name = name
        self.age = age
        self.__salary = salary  # Encapsulation: Private attribute

    def get_salary(self):
        """Provide access to the private salary attribute."""
        return self.__salary

    def set_salary(self, new_salary):
        """Update the private salary attribute with validation."""
        if new_salary > 0:
            self.__salary = new_salary
        else:
            raise ValueError("Salary must be positive.")

    def work(self):
        """General method to represent work."""
        return f"{self.name} is working."

    def calculate_annual_salary(self):
        """Calculate and return the annual salary."""
        return self.__salary * 12

# Subclass: Manager
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        """Initialize Manager with additional department attribute."""
        super().__init__(name, age, salary)
        self.department = department

    def work(self):
        """Override work method to specify manager's task."""
        return f"{self.name} is managing the {self.department} department."

    def calculate_bonus(self):
        """Calculate a 10% bonus on the annual salary."""
        return self.calculate_annual_salary() * 0.1

# Subclass: Developer
class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        """Initialize Developer with additional programming_language attribute."""
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def work(self):
        """Override work method to specify developer's task."""
        return f"{self.name} is writing code in {self.programming_language}."

    def calculate_overtime_pay(self, hours):
        """Calculate overtime pay at 1.5x the hourly rate."""
        hourly_rate = self.get_salary() / 160  # Assuming 160 hours/month
        return hours * hourly_rate * 1.5

# Subclass: Intern
class Intern(Employee):
    def __init__(self, name, age, salary, duration):
        """Initialize Intern with additional duration attribute."""
        super().__init__(name, age, salary)
        self.duration = duration

    def work(self):
        """Override work method to specify intern's task."""
        return f"{self.name} is working as an intern for {self.duration} months."

    def calculate_stipend(self):
        """Calculate total stipend based on duration."""
        return self.get_salary() * self.duration

# Polymorphism: A function that works with any type of Employee
def employee_work(employee):
    print(employee.work())

# Main function
def main():
    # Create objects for different employee types
    manager = Manager("Alice", 45, 90000, "HR")
    developer = Developer("Bob", 30, 80000, "Python")
    intern = Intern("Charlie", 22, 20000, 6)

    # Print salaries for all employees
    print(f"Manager's salary: {manager.get_salary()}")
    print(f"Developer's salary: {developer.get_salary()}")
    print(f"Intern's salary: {intern.get_salary()}")

    # Update and print the manager's salary
    manager.set_salary(95000)
    print(f"Updated Manager's salary: {manager.get_salary()}")

    # Compute and display bonus, stipend, and overtime
    print(f"Manager's bonus: {manager.calculate_bonus()}")
    print(f"Developer's overtime pay for 10 hours: {developer.calculate_overtime_pay(10)}")
    print(f"Intern's total stipend: {intern.calculate_stipend()}")

    # Demonstrate polymorphism
    employees = [manager, developer, intern]
    for emp in employees:
        employee_work(emp)

# Ensure the main function runs only when executed as a script
if __name__ == "__main__":
    main()
