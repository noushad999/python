
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
