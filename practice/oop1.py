#problem solve:
#1.define a circle class to create a circle with radius r using the constructor.
#define an area() method of the class which calculates the area of the circle
#define a perimeter() method of the class which allowes tou to calculate the perimeter of the circle

# class circle:
#     def __init__(self,r):
#         self.r=r
    
#     def area(self):
#         return (22/7)*self.r**2
    
#     def perimeter(self):
#         return 2*(22/7)*self.r

# c1=circle(21)
# print(c1.area())
# print(c1.perimeter())

#2.define a employee class with attributes role,department and salary .this class also have class showDetails() method

# class employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary
    
#     def showDetails(self):
#         print("Role:",self.role)
#         print("Department:",self.department)
#         print("Salary:",self.salary)

# class engineer(employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("engineer","IT",60000)

# e1=employee("developer","IT",50000)
# e1.showDetails()

# e2=employee("tester","IT",40000)
# e2.showDetails()

# eng1=engineer("noushad",25)
# eng1.showDetails()
#now create an engineer class that inherits properties from employee and has an additional attribute called :name and age

#3.create a class called order which stores item and its price
#use dunder funtion __gt__() to convey that:
#order1>order2 if price of order1>order2

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price>odr2.price
    
odr1=order("laptop",50000)
odr2=order("mobile",20000)

print(odr1>odr2)