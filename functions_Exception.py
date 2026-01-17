#Mutation #Functions
#Read a given string, change the character at a given index and then print the modified string.
def mutate_string(string, position, character):
    #string=string[:5]+character+string[6:] 
    l=list(string)
    l[position]=character
    string=''.join(l)
    return string
print(mutate_string('Abasdfdgsf',6,'Z'))

#Write a program to generate series up to n.
def seri(n1,n2,n3,n4):
    fn=0
    fn1=fn+n1
    fn2=n1+n2
    fn3=n2+n3
    fn4=n3+n4
    return fn1,fn2,fn3,fn4
print(list(seri(1,2,3,4)))
#Write a program to  fibconaic series nth term.
def fib_ser(n):
        if n<=1: 
            return n
        else:
            nth=fib_ser(n-1)+fib_ser(n-2)
            return nth 
term=11
print(f"the {term} of fibconaic series is:{fib_ser(term)}")

#Calculate factorial 
def fac(n:int): #only integer are passed
     fact=1
     for i in range(1,n+1):
          fact=fact*i
          print(f'the factorial of a number is:{fact}')
fac(10)
#Convert doller into Rupees
def convert(amount,symb):
     try:
        if symb == "$":
          amount*=270
          rupee=amount
          print(f'convert into Rupees:{rupee}')
        if symb =='/-':
          amount/=270
          dollar=amount
          print(f'convert into dollar{dollar}')
     except:
         print("Working not start")
Amount_enter=int(input())
convert(Amount_enter,'/-')

#Write a program to simulate a simple ATM 1.Check balance 2.Deposit money 4.Withdraw money
def atm_simu():
     balance=1000
     try:
          select_opera=int(input())
     except:
          print("Kindly Enter vaild number b/w(1-3)")
     try:
          if select_opera==1: #1.Check balance
               print(f"Your current balance is:{balance}")
          elif select_opera==2: #2.Deposit money
               deposit=int(input())
               balance+=deposit
               print(f"Amount deposit:{balance}")
          elif select_opera==3: #4.Withdraw money
               withdraw=int(input())
               balance-=withdraw
               print(f"Amount Withdraw:{balance}")
     except:
          print("kindly select suitable operations!")

atm_simu() #function invoke

#lambda function
add_lambda=lambda a,b,c:a+b/c
print(add_lambda(1,2,2))

#Recursive functions
def multi(a):
     if a>100: #base class
        return
     print(a)
     multi(a*2)
multi(3)
#factorial recursive task
def fact(n):
     if n==1 or n==0:#base case
          return 1
     else:
          return n*fact(n-1) #function called again
print(fact(3))
#sum of first n number
def sum(n):
    if n<=0:
         return 0  #neccassary to return value 
    else:
         return n + sum(n-1) # never call same function value
print(sum(3))
#Generators
def online_order(order:list):
    #  a=order[2] 
    #  yield a (Generator execute once time and take a pause ) 
     yield order[3]
accessing_value=online_order([1,2,3,4,5])
print(next(accessing_value))

   

