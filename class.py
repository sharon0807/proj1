class GFG:
    def __init__(somename, name, company):
        somename.name = name
        somename.company = company

    def show(somename):
        print("Hello my name is " + somename.name +
              " and I work in "+somename.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()

class Dog:

    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

#What self Represents:
#Instance Methods: In instance methods (methods defined inside a class), self refers to the instance of the class. When you call an instance method on an object, Python automatically passes the instance (self) as the first argument to the method.

#instance Variables: Within the methods of a class, self is used to access instance variables (attributes) that belong to that particular instance.
class MyClass:
    def __init__(self, x):
        self.x = x  # 'self.x' is an instance variable

    def print_x(self):
        print(self.x)  # Accessing instance variable 'x' using 'self'

# Creating an object of MyClass
obj = MyClass(42)

# Calling instance method 'print_x' on the object 'obj'
obj.print_x()  # Output: 42

"""class Employee:
    def __init__(self, name, age, id, salary):
        # Initializing the attributes of the class
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

# Creating objects of the Employee class
emp1 = Employee("harshit", 22, 1000, 1234)
emp2 = Employee("arjun", 23, 2000, 2234)

# Printing the dictionary representation of emp1
print(emp1.__dict__)
"""

#single inheritance
# This is a parent class
class employee1:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# This is a child class
class childemployee(employee1):
    def __init__(self, name, age, salary, id):
        # Initialize the attributes from the parent class
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

# Creating an object of the parent class
emp1 = employee1('harshit', 22, 1000)
print(emp1.age)  #
"""
# multilevel inheritance
# This is a parent class
class employee1:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# This is a child class
class childemployee(employee1):
    def __init__(self, name, age, salary, id):
        # Initialize the attributes from the parent class
        super().__init__(name, age, salary)
        self.id = id

# Creating an object of the parent class
emp1 = employee1('harshit', 22, 1000)
print(emp1.age)  #

# This is a parent class
class employee1:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# This is a child class
class childemployee(employee1):
    def __init__(self, name, age, salary,id):
        # Initialize the attributes from the parent class
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

# Creating an object of the parent class
emp1 =childemployee('harshit', 22, 1000,3)
print(emp1.age)  #

# This is a parent class
class employee1:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# This is a child class
class childemployee(employee1):
    def __init__(self, name, age, salary, id):
        # Manually initialize the attributes from the parent class
        employee1.__init__(self, name, age, salary)
        self.id = id

# Creating an object of the parent class
emp1 = employee1('harshit', 22, 1000)
print(emp1.age)  # Output: 22

# Creating an object of the child class
emp2 = childemployee('arjun', 23, 2000, 2234)
print(emp2.id)  # Output: 2234
print(emp2.name)  # Output: arjun

#hierarchical
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class ChildEmployee1(Employee):
    def __init__(self, name, age, salary):
        Employee.__init__(self, name, age, salary)

class ChildEmployee2(Employee):
    def __init__(self, name, age, salary):
        Employee.__init__(self, name, age, salary)
        
emp1 = Employee('harshit', 22, 1000)
emp2 = Employee('arjun', 23, 2000)

print(emp1.name, emp1.age, emp1.salary)
print(emp2.name, emp2.age, emp2.salary)

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class ChildEmployee1(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

class ChildEmployee2(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

emp1 = Employee('harshit', 22, 1000)
emp2 = Employee('arjun', 23, 2000)

print(emp1.name, emp1.age, emp1.salary)
print(emp2.name, emp2.age, emp2.salary)

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class ChildEmployee1(Employee):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
class ChildEmployee2(Employee):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
emp1 = Employee('harshit', 22, 1000)
emp2 = Employee('arjun', 23, 2000)

print(emp1.name, emp1.age, emp1.salary)
print(emp2.name, emp2.age, emp2.salary)

multiple:
class Employee1:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Employee2:
    def __init__(self, name, age, salary, id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

class ChildEmployee(Employee1, Employee2):
    def __init__(self, name, age, salary, id):
        super().__init__(name, age, salary)
        self.id = id

# Creating instances of the classes
emp1 = Employee1('harshit', 22, 1000)
emp2 = Employee2('arjun', 23, 2000, 1234)
emp3 = ChildEmployee('alex', 25, 1500, 5678)

# Accessing attributes
print(emp1.name, emp1.age, emp1.salary)  # Output: harshit 22 1000
print(emp2.name, emp2.age, emp2.salary, emp2.id)  # Output: arjun 23 2000 1234
print(emp3.name, emp3.age, emp3.salary, emp3.id)  # Output: alex 25 1500 5678

class Employee1:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Employee2:
    def __init__(self, name, age, salary, id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

class ChildEmployee(Employee1, Employee2):
    def __init__(self, name, age, salary, id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
        

# Creating instances of the classes
emp1 = Employee1('harshit', 22, 1000)
emp2 = Employee2('arjun', 23, 2000, 1234)
emp3 = ChildEmployee('alex', 25, 1500, 5678)

# Accessing attributes
print(emp1.name, emp1.age, emp1.salary)  # Output: harshit 22 1000
print(emp2.name, emp2.age, emp2.salary, emp2.id)  # Output: arjun 23 2000 1234
print(emp3.name, emp3.age, emp3.salary, emp3.id)  # Output: alex 25 1500 5678

class Employee1:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Employee2:
    def __init__(self, name, age, salary, id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

class ChildEmployee(Employee1, Employee2):
    def __init__(self, name, age, salary, id):
        Employee1.__init__(self, name, age, salary)
        Employee2.__init__(self, name, age, salary, id)

# Creating instances of the classes
emp1 = Employee1('harshit', 22, 1000)
emp2 = Employee2('arjun', 23, 2000, 1234)
emp3 = ChildEmployee('alex', 25, 1500, 5678)

# Accessing attributes
print(emp1.name, emp1.age, emp1.salary)  # Output: harshit 22 1000
print(emp2.name, emp2.age, emp2.salary, emp2.id)  # Output: arjun 23 2000 1234
print(emp3.name, emp3.age, emp3.salary, emp3.id)  # Output: alex 25 1500 5678

"""
#polymorphism
#compile time
class Employee1:
    def name(self):
        print("Harshit is his name")

    def salary(self):
        print("3000 is his salary")

    def age(self):
        print("22 is his age")

class Employee2:
    def name(self):
        print("Rahul is his name")

    def salary(self):
        print("4000 is his salary")

    def age(self):
        print("23 is his age")

def func(obj):
    obj.name()
    obj.salary()
    obj.age()

# Create instances of Employee1 and Employee2
obj_emp1 = Employee1()
obj_emp2 = Employee2()

# Call func with different objects
func(obj_emp1)
print("---")
func(obj_emp2)

class Employee:
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

    def earn(self):
        pass

class ChildEmployee1(Employee):
    def earn(self):
        print("No money")

class ChildEmployee2(Employee):
    def earn(self):
        print("Has money")

# Create instances of ChildEmployee1 and ChildEmployee2
c = ChildEmployee1('Alice', 25, 1234, 0)
d = ChildEmployee2('Bob', 30, 5678, 5000)

# Call the earn method to demonstrate polymorphism
c.earn()  # Output: No money
d.earn()  # Output: Has money

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")

class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph")

class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph")

class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph")

# Driver code
t = Tesla()
t.mileage()  # Output: The mileage is 30kmph

r = Renault()
r.mileage()  # Output: The mileage is 27kmph

s = Suzuki()
s.mileage()  # Output: The mileage is 25kmph

d = Duster()
d.mileage()  # Output: The mileage is 24kmph

class Base1:
    def __init__(self):
        # The protected member
        self._p = 78

# Derived class
class Derived1(Base1):
    def __init__(self):
        # Call the constructor of Base1
        super().__init__()  # Preferred way to call the parent class constructor
        print("We will call the protected member of base class: ", self._p)
        
        # Modify the protected member
        self._p = 433
        print("We will call the modified protected member outside the class: ", self._p)

# Create instances of the classes
obj_1 = Derived1()
obj_2 = Base1()

# Access the protected member
# This can be accessed but it should not be done because of convention
print("Access the protected member of obj_1: ", obj_1._p)

# Access the protected member of obj_2
print("Access the protected member of obj_2: ", obj_2._p)

class Base1:
    def __init__(self):
        self.p = "Pythonpoint"
        self.__q = "Pythonpoint"

    def get_private(self):
        return self.__q

# Creating a derived class
class Derived1(Base1):
    def __init__(self):
        # Calling constructor of Base class
        super().__init__()
        print("We will call the private member of the base class using a public method: ")
        print(self.get_private())

# Driver code
obj_1 = Base1()
print(obj_1.p)  # This will print: Pythonpoint

obj_2 = Derived1()  # This will print the private member using a method in the base class
