                                                  #Task 1

# class Book:
#     def __init__(self,title,author,year,isbm):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.isbm = isbm

#     def info(self):    
#         return f"Title: {self.title}, Author: {self.author}, year: {self.year} isbm: {self.isbm}"

#     def is_older_than(self, years):
#         current_year = 2024
#         return current_year - self.year > years > years
    
# book = Book("2024","John Makets", 2023, "213124.124")
# print(book.info())
# print("Is the book older than 20 years?", book.is_older_than(20))


                                                    #Task 2

# class BankAccount:
#     def __init__(self,balance,amount,holder):
#         self.balance = balance

#     def getBalance(self,balance):
#         self.balance = balance

#     def getAmount(self,amount):
#         self.balance += amount
#         self.balance += amount

#     def holder(self,holder):
#         self.balance = holder
#         self.balance = holder

#     def total(self):
#         return self.balance
# akk = BankAccount(200,400,600, "John")

# akk.getAmount(50)
# print(akk.total())

                                                #Task 3

# class Student:
#     def __init__(self,name,student_id,grades):
#         self.name = name
#         self.student_id = student_id
#         self.grades = grades

#     def text(self):
#         return f"Heello my name is {self.name}, my student id is {self.student_id}, and i get grades {self.grades}"
    
# student = Student("Jack", "M2543", "5")  
# print(student.text())  
    

                                               #Task 4
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# class CarPark:
#     def __init__(self):
#         self.cars = []
    
#     def add_car(self, car):
#         self.cars.append(car)
    
#     def remove_car(self, car):
#         self.cars.remove(car)
    
#     def display_cars(self):
#         for car in self.cars:
#             print(f"{car.make} {car.model} ({car.year})")         

# car1 = Car("Toyota", "Supra A80", "2002")
# car2 = Car("Nissan", "GTR R34", "2007")            

# park = CarPark()
# park.add_car(car1)
# park.add_car(car2)

# park.display_cars()

                                                    #Task5
# class Character:
#     def __init__(self,name,health,attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power

#     def text(self):
#         return f"Name: {self.name}, Health: {self.health}, Attack power: {self.attack_power}"
    
# class Mage(Character):
#     def __init__(self,name,health,mag_power):
#         super().__init__(name,health, 0)
#         self.mag_power = mag_power

#     def text_mage(self):
#         return f"Name: {self.name}, Health: {self.health}, Mag Power: {self.mag_power}"  

# class Warrior(Character):
#     def __init__(self,name,health,physical_power):
#         super().__init__(name,health, 0)
#         self.physical_power = physical_power

#     def text_warrior(self):
#         return f"Name: {self.name}, Health: {self.health}, Physical Power: {self.physical_power}"

# mage = Mage("Frostbite", 150, "MG DMG 2000")      
# print(mage.text_mage())
# print("   ")
# print(mage.text_mage())
# warrior = Warrior("Frostfury", 120, "Crit DMG 5000")
# print(warrior.text_warrior())
# print("   ")
# print(warrior.text_warrior())

                                                       #Task 6

# import math

# class Shape:
#     def __init__(self,color):
#         self.color = color

#     def area(self):
#         return f"Color: {self.color}"
    
# class Circle(Shape):
#     def __init__(self,color,radius):
#         super().__init__(color)
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)
    
# class  Rectangle(Shape):
#     def __init__(self,color,width,height):
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Triangle(Shape):
#     def __init__(self,color,base,height):
#         super().__init__(color)
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# circle = Circle("Red", 5)
# rectangle = Rectangle("Blue", 4, 6)
# triangle = Triangle("White", 5, 9)
  
# print(f"Circle area: {circle.area()}, (Color: {circle.color})")
# print(f"Rectangle area: {rectangle.area()}, (Color: {rectangle.color})")
# print(f"Triangle area: {triangle.area()}, (Color: {triangle.color})")

                                                  #Task 7
# I DIDN'T UNDERSTAND QUESTION AND ALSO I IDK HOW TO DO IT :)