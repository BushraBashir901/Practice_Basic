#Nested Loop
for i in range(3,5): #3,4 run
    for j in range(1,2): #only 1 run
        print(f'{i},{j}')
#Break
alpha=['a','b','c','d','e']
for i in alpha:
    for j in range(0,4):
         print(f'{i},{j}')
    break  #only one time loop execute 
#Continue
alpha1=['a','b','c','d','e']
for i in alpha1:
    for j in range(0,4): # excute on given range 0,1,2,3
         if j==2:  #skip 2 iteration
              continue #skip this iteration 
         print(f'{i},{j}')
         if j==0:
             pass #use later
#user input
for i in range(1,11): #1,2,3,4,5,6,7,8,9,10
     if i%2==0:
        print(f'{i}')
     elif i%2!=0: #skip 1,3,5,7,9
        continue
print("Excuted")
#######
start=int(input())
stop=int(input())
skip=int(input())
for i in range(start,stop): #i is variable which is used/apply on loop
    if i==skip:
        continue
    print(f'remaning values are:{i}')
#string method
def solve(s): #string 1st letter capital
    return s.title()
s=input()
print(solve(s))

swap=input().swapcase() #covert lower to upper and upper to lower
print(swap)

st='Here is problem'
print(st.replace('Here','there')) # replace with new word

st1='He She It'
v=st1.split(' ') #spilting method
print(v)
jo=' '.join(st1)
print(jo)
#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    # write your code here
    a=line.split(" ") #convert string into list like line=['this','is','code']
    b="-".join(a) #convert list into string by joining hyphen
    return b

nested=[1,2,3,True] #Nested list
sec=['a','b','f',nested,[2,3,4,5,6]]
print(sec)

constructor_list=list(range(0,50,5)) #list creating through constructor method
print(constructor_list)

#Dictionary
Books={
    'depart':'Cs',
    'Eng':['Mr.chips','Mr.chemist'],
    'math':['integration','differential','Algerba'],
    'subj_count':2,
    'sec':'A'
}
for h in Books.pop('sec'): #show which value is remove
    print(h)

for e in Books.items(): #show items(keys:value) inthe form of tuple 
    print(e)
for k in Books: #loop applied on Dictionary and get keys
    print(k)

print(Books)
Books['subj_count']=Books['subj_count']*4 #Updated Books dictionary 
print(Books)

#Functions
def day(): #simple
    print("hi")
day()
def num(a,b): #parametirzed 
    print(f'numbers are:{a},{b}')
num(2,3)
def subj(eng,math,phy): #positioning argument->position must be same (parame==argu)
    print(f"these are subj:{eng},{math},{phy}")
subj('Mr.chips','geometry','work') 

def subj(eng='Mr.chips',math='geometry',phy='work'): #default values pass (start from end to give default value)
    print(f"these are subj:{eng},{math},{phy}")
subj() # updated value can be pass here

#Create a function that returns the square of a number.
def squ(i):
    sq_num=i*i
    return sq_num #send value back from a function
print(squ(3))
#Average of 2 numbers
def avg(start,end):
    avg_nmb=(start+end)/2
    print(avg_nmb)
avg(2,6)
avg(123,456)
#Length of list
def len_lis(List):
    L=len(List)
    return L
List=[1,2,3,4,5,6,7,8,9,10]
print(len_lis(List))
#print elements of list in single line
def elem_list(lis):
    for i in lis:
        print(i,end=' ')
lis=['a','b','c']
elem_list(lis)


#Write a function that takes a list of numbers and returns the maximum value.
def list_num(list): #Need to set out
    max_num=list[0]
    for i in list:
        if max_num<i:
            print(list_num)
list=[1,2,3,4]   
print(list_num(list))





