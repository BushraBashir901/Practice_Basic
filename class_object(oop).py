class Atm:
    def __init__(self):
        self.pin="" #data of class
        self.balance=0 #data of class
        print(id(self)) #want to print reference/address  

        self.menu()  #behaviour of class
         
    def menu(self): #Method for menue
        while True:
         user_input=input('''
                    Hello Customers!Select pin
                         1.Create pin
                         2.Deposit Money
                         3.Withdraw
                         4.Check Balance
                         5.Exit 
                         ''')
         if user_input=='1':
            self.create()
         elif user_input=='2':
            self.deposit()
         elif user_input=='3':
            self.withdraw()
         elif user_input=='4':
            self.check_balance()
            break
         else:
            print("Exit")
    def create(self):
        try:
         self.pin=int(input("Create Your ATM card pin")) # or create_pin=int(input()) 
        except:
            if self.pin==None:
             print("Enter valid pin(0-9)")
    def deposit(self):
        #Check authentication before depositing
        enter_pin=int(input("Enter Your ATM pin"))
        if enter_pin==self.pin:
            amount_deposit=int(input("Enter the Amount you want to deposit"))
            self.balance+=amount_deposit
            print(f"deposit amount{self.balance}")
    def withdraw(self):
        #Check authentication before withdraw
        enter_pin=int(input("Enter Your ATM pin"))
        if enter_pin==self.pin:
            amount_withdraw=int(input("Enter the Amount you want to withdraw"))
            if amount_withdraw<=self.balance:
               self.balance-=amount_withdraw
               print(f"Withdraw amount:{self.balance}")
            else:
               print("Please Valid Amount")
        else:
           print("Invaild Pin")
        
    def check_balance(self):
        #Check authentication before checking Balance
        enter_pin=int(input("Enter Your ATM pin"))
        if enter_pin==self.pin:
           print(f"your current balance is:{self.balance}")
        else:
           print("Enter Valid Pin")
    
atm=Atm()  

#Creating own datatypes
class Fraction:
   def __init__(self,n,d):
      self.num=n
      self.den=d
   def __str__(self):
      #Magic method thats why its automatically called
      return "{}/{}".format(self.num,self.den) #format() used to provide format of printing
   def __add__(self,other): #add two objects 
      temp_num=self.num*other.den + other.num*self.den
      temp_den=self.den*other.den 
      return "{}/{}".format(temp_num,temp_den)
   def __sub__(self,other): #subtract two objects in format of fraction
      temp_num1=self.num*other.den - other.num*self.den
      temp_den1=self.den*other.den 
      return "{}/{}".format(temp_num1,temp_den1)
   def __mul__(self,other): #Multiple two objects in format of fraction
      temp_num1=self.num*other.den
      temp_den1=self.den*other.den 
      return "{}/{}".format(temp_num1,temp_den1)
   
    
fr=Fraction(2,3)  
ad=Fraction(3,2)   
print(fr+ad)
print(fr-ad)
print(fr*ad)

        
