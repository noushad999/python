
### **Object-Oriented Programming (OOP)**

1. **Class and Object**  
   - **Class**: A blueprint for creating objects (a collection of attributes and methods).  
   - **Object**: An instance of a class.

   **Syntax**:
   ```python
   class ClassName:
       # Class attributes and methods
       pass
   ```

   **Example**:
   ```python
   class Car:
       color = "black"
       brand = "BMW"
   
   car1 = Car()
   print(car1.color)  # Output: black
   print(car1.brand)  # Output: BMW
   ```

2. **Constructor**  
   - A special method used to initialize the object when it is created.
   - Defined using `__init__(self)`.

   **Example**:
   ```python
   class Student:
       def __init__(self, name, age):
           self.name = name
           self.age = age
           print("Student added to database")

   s1 = Student("Noushad", 20)
   print(s1.name, s1.age)  # Output: Noushad 20
   ```

3. **Attributes**  
   - **Object Attribute**: Specific to each object, defined using `self.attribute_name`.
   - **Class Attribute**: Shared by all objects, defined as `ClassName.attribute_name`.

   **Example**:
   ```python
   class Student:
       college_name = "ABC College"  # Class attribute

       def __init__(self, name, age):
           self.name = name  # Object attribute
           self.age = age

   s1 = Student("Noushad", 20)
   print(s1.name, s1.age, s1.college_name)  # Output: Noushad 20 ABC College
   ```

4. **Methods**  
   - Functions defined inside a class to perform specific tasks.
   - **Object Method**: Operates on the specific object.  
     **Example**:
     ```python
     class Student:
         def __init__(self, name):
             self.name = name

         def greet(self):
             print(f"Hello, {self.name}")

     s1 = Student("Noushad")
     s1.greet()  # Output: Hello, Noushad
     ```

   - **Static Method**: Does not operate on any object or class attribute. Defined using `@staticmethod`.  
     **Example**:
     ```python
     class Utility:
         @staticmethod
         def greet():
             print("Hello, World!")

     Utility.greet()  # Output: Hello, World!
     ```

5. **Four Pillars of OOP**  
   - **Abstraction**: Hiding complexity and showing only the essential features.  
     **Example**:
     ```python
     class Car:
         def start(self):
             print("Car started")
     
     car1 = Car()
     car1.start()  # Output: Car started
     ```
   - **Encapsulation**: Wrapping data and methods into a single unit to restrict direct access to data.  
     **Example**:
     ```python
     class Account:
         def __init__(self, balance):
             self.__balance = balance  # Private attribute
         
         def get_balance(self):
             return self.__balance
     
     acc = Account(1000)
     print(acc.get_balance())  # Output: 1000
     ```
   - **Inheritance**: Allowing one class to inherit attributes and methods of another class.  
     **Example**:
     ```python
     class Animal:
         def sound(self):
             print("Animal makes a sound")
     
     class Dog(Animal):
         def sound(self):
             print("Dog barks")
     
     d = Dog()
     d.sound()  # Output: Dog barks
     ```
   - **Polymorphism**: One name, multiple forms (e.g., method overriding).  
     **Example**:
     ```python
     class Shape:
         def area(self):
             pass

     class Circle(Shape):
         def area(self, radius):
             return 3.14 * radius * radius

     class Rectangle(Shape):
         def area(self, length, breadth):
             return length * breadth

     c = Circle()
     print(c.area(5))  # Output: 78.5

     r = Rectangle()
     print(r.area(4, 6))  # Output: 24
     ```

6. **Practice Example**: Bank Account
   ```python
   class Account:
       def __init__(self, balance, account_no):
           self.balance = balance
           self.account_no = account_no

       def debit(self, amount):
           if amount > self.balance:
               print("Insufficient funds")
           else:
               self.balance -= amount
               print(f"{amount} debited. Current balance: {self.balance}")

       def credit(self, amount):
           self.balance += amount
           print(f"{amount} credited. Current balance: {self.balance}")

       def get_balance(self):
           return self.balance

   acc1 = Account(2000, 123456)
   acc1.debit(500)
   acc1.credit(300)
   print("Final Balance:", acc1.get_balance())
   ```



### **1. `del` Keyword**
- The `del` keyword is used to delete properties of an object or the object itself from memory.

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Noushad")
print(s1.name)  # Output: Noushad

del s1.name  # Deleting the 'name' property
# print(s1.name)  # This will raise an AttributeError because 'name' is deleted.
```

---

### **2. Private Attributes**
- Attributes prefixed with `__` are treated as private and are not accessible directly outside the class.

```python
class Account:
    def __init__(self, acc_no, acc_pass):
        self.__acc_no = acc_no  # Private attribute
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)  # Accessing private attribute inside the class

acc1 = Account(1234, 5880)
# print(acc1.__acc_no)  # AttributeError
```

---

### **3. Private Methods**
- Methods prefixed with `__` are private and can only be accessed within the class.

```python
class Person:
    __name = "Anonymous"

    def __hello(self):  # Private method
        print("Hello, World!")

    def welcome(self):
        self.__hello()  # Private method called inside the class

p1 = Person()
p1.welcome()  # Output: Hello, World!
# p1.__hello()  # AttributeError
```

---

### **4. Inheritance**
Inheritance allows one class (child) to use properties and methods of another class (parent).

#### **4.1 Single Inheritance**
```python
class Car:
    @staticmethod
    def start():
        return "Car started"

    @staticmethod
    def stop():
        return "Car stopped"

class BMW(Car):
    def __init__(self, name):
        self.name = name

car1 = BMW("A Series")
print(car1.start())  # Output: Car started
```

#### **4.2 Multilevel Inheritance**
```python
class Car:
    @staticmethod
    def start():
        return "Car started"

class BMW(Car):
    def __init__(self, name):
        self.name = name

class BMW1(BMW):
    def __init__(self, car_type):
        self.car_type = car_type

car1 = BMW1("Octane")
print(car1.start())  # Output: Car started
```

#### **4.3 Multiple Inheritance**
```python
class A:
    varA = "Welcome to Class A"

class B:
    varB = "Welcome to Class B"

class C(A, B):
    varC = "Welcome to Class C"

c1 = C()
print(c1.varA)  # Output: Welcome to Class A
print(c1.varB)  # Output: Welcome to Class B
print(c1.varC)  # Output: Welcome to Class C
```

---

### **5. `super()` Method**
- Used to call the parent class's constructor or methods in the child class.

```python
class Car:
    def __init__(self, car_type):
        self.car_type = car_type

class ToyotaCar(Car):
    def __init__(self, name, car_type):
        super().__init__(car_type)  # Calling parent class constructor
        self.name = name

car1 = ToyotaCar("Prius", "Electric")
print(car1.car_type)  # Output: Electric
```

---

### **6. Class Methods**
- Class methods are methods that can access and modify class-level data.
- Declared using the `@classmethod` decorator.

```python
class Person:
    name = "Anonymous"

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name

p1 = Person()
p1.change_name("Noushad")
print(Person.name)  # Output: Noushad
```

---

### **7. Property Decorator**
- Allows us to define a method as a property that can be accessed like an attribute.

```python
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return (self.phy + self.chem + self.math) / 3

stu1 = Student(88, 99, 77)
print(stu1.percentage)  # Output: 88.0

stu1.phy = 95
print(stu1.percentage)  # Output: 90.33
```

---

### **8. Polymorphism**
- The ability of an object to take on many forms, such as using the same method name in different classes.

---

### **9. Operator Overloading**
- Using special methods (dunder methods) to define behavior for operators.

```python
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)

    def show(self):
        print(f"{self.real} + {self.img}j")

num1 = Complex(2, 3)
num2 = Complex(1, 4)

result = num1 + num2
result.show()  # Output: 3 + 7j
```

---

### **10. Dunder Methods**
- Special methods with double underscores used for operator overloading and other special functionalities.
- Examples:
  - `__add__`: For addition (`+`)
  - `__sub__`: For subtraction (`-`)
  - `__mul__`: For multiplication (`*`)

---

### ***Problem Solving***

### **1. Define a Circle Class**
**Problem Statement:**  
Define a `Circle` class to create a circle with radius `r` using the constructor. Define an `area()` method of the class which calculates the area of the circle. Define a `perimeter()` method of the class which allows you to calculate the perimeter of the circle.

**Solution:**
```python
class Circle:
    def __init__(self, radius):
        """
        Initialize the Circle object with the given radius.
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate and return the area of the circle.
        Formula: π * r^2
        """
        return (22 / 7) * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.
        Formula: 2 * π * r
        """
        return 2 * (22 / 7) * self.radius

# Example usage
circle1 = Circle(21)
print("Area of Circle:", circle1.area())
print("Perimeter of Circle:", circle1.perimeter())
```

---

### **2. Define an Employee Class**
**Problem Statement:**  
Define an `Employee` class with attributes `role`, `department`, and `salary`. This class also has a `showDetails()` method. Now create an `Engineer` class that inherits properties from `Employee` and has additional attributes called `name` and `age`.

**Solution:**
```python
class Employee:
    def __init__(self, role, department, salary):
        """
        Initialize the Employee object with the given attributes.
        """
        self.role = role
        self.department = department
        self.salary = salary
    
    def show_details(self):
        """
        Display the details of the employee.
        """
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        """
        Initialize the Engineer object with additional attributes.
        Inherit role, department, and salary from the Employee class.
        """
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 60000)  # Default values for Engineer class

    def show_details(self):
        """
        Display the details of the engineer.
        """
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_details()

# Example usage
employee1 = Employee("Developer", "IT", 50000)
employee1.show_details()

print("\n")

engineer1 = Engineer("Noushad", 25)
engineer1.show_details()
```

---

### **3. Define an Order Class**
**Problem Statement:**  
Create a class called `Order` which stores `item` and its `price`. Use the dunder function `__gt__()` to convey that:  
`order1 > order2` if the price of `order1` > price of `order2`.

**Solution:**
```python
class Order:
    def __init__(self, item, price):
        """
        Initialize the Order object with the given item and price.
        """
        self.item = item
        self.price = price

    def __gt__(self, other_order):
        """
        Compare two orders based on their price.
        Returns True if the current order's price is greater than the other order's price.
        """
        return self.price > other_order.price

# Example usage
order1 = Order("Laptop", 50000)
order2 = Order("Mobile", 20000)

if order1 > order2:
    print(f"{order1.item} is more expensive than {order2.item}.")
else:
    print(f"{order2.item} is more expensive than {order1.item}.")
```

---

### **Output Examples**
#### **1. Circle Class Output**
```
Area of Circle: 1386.0
Perimeter of Circle: 132.0
```

#### **2. Employee and Engineer Classes Output**
```
Role: Developer
Department: IT
Salary: 50000


Name: Noushad
Age: 25
Role: Engineer
Department: IT
Salary: 60000
```

#### **3. Order Class Output**
```
Laptop is more expensive than Mobile.
```

---
###***The End Of OOP***
---

