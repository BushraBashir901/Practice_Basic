#Pass by Reference
class Customer:
    #class/static variables (used when we want to apply loop like operations)
    cust_id=0
    def __init__(self,name,gender,Age):
        self.name=name
        self.gender=gender
        self.age=Age
        self.id=Customer.cust_id
        Customer.cust_id=Customer.cust_id+1
    @staticmethod  #No self parameter will be pass
    def hello():
         print("hellosss")
def greeting(for_customer): #function outside the class but we use there parameter data in there function .And these have multiple parameter like name,gender
    if for_customer.gender=="Male":
        print(f"Salaam! {for_customer.name} sir")
    else:
          print(f"Salaam! {for_customer.name} Maam")
    if for_customer.age<=18: #we can only use parameter of __init__if call through for_customer.
        print(f"Salaam! {for_customer.name} child")
    else:
          print(f"Salaam! {for_customer.name} Adult")
cust=Customer("Ali",'Male',12)
print(cust.name)
greeting(cust) #use object of a class in function 

cust1=Customer("Ahmad",'Male',25)
cust2=Customer("hammad",'Male',21)
cust3=Customer("Basit",'Male',30)
print(cust1.id,cust2.id,cust3.id)
print(cust.cust_id)

#Collection of objects in a list 
c=[cust,cust2,cust3]
for i in c:
    i.hello()  

#Abstraction
from abc import ABC,abstractmethod
class Vehicle(ABC):  # Abstract class
    @abstractmethod
    def start(self):
        pass  # Abstract method

class Car(Vehicle):
    def start(self):
        print("Car engine started")

c = Car()
c.start()

#Inheritance
class Animal: #parent
    @staticmethod
    def Eat():
        print("eat the food")
    @staticmethod
    def Drink():
        print("drink the water")
class Birds: #parent
    @staticmethod
    def fly():
        print("birds can fly")

class Organism(Animal,Birds): #multiple
    @staticmethod
    def charactersitc():
        pass
o=Organism()
print(o.fly)

class Cat(Animal): #single inheritance
    @staticmethod
    def sleep():
        print("Sleep")
class Dog(Cat): #Multi-level Inheritance
    @staticmethod
    def bark():
        print("barking")
animal=Animal()
dog=Dog()
animal.Drink()
animal.Eat()
dog.sleep()
dog.Drink()
#MRO View
print(Dog.__mro__) #inthe form of tuple
print(Dog.mro()) #inthe form of list
help(Dog)

