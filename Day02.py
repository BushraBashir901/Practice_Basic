#+++++++++++++++++Day 02++++++++++++++++++++++++++++#
#...................List................................#
List=[] #taking input and adding 3 movies into list
movie1=input()
movie2=input()
movie3=input()
List.append(movie1)
List.append(movie2)
List.append(movie3)
print(List)

chck_list=[1,2,3,4,5,4,3,2,1] #checking Pallindrom
copy_list=chck_list.copy()
copy_list.reverse()
if chck_list==copy_list:
    print("True")
else:
    print("False")

grade=('A','F','D','B','A') #Count the number of grades of a student
count=grade.count('A')
print(count)
store=list(grade)
store.sort()
print(store)
print("problems")

# N = input("Enter the iteration of command")
# empty_li=[]
# for itera in range(N):
#     my_lis=input().split()
#     if my_lis[0]=='insert':
#         empty_li.insert(my_lis[1],my_lis[2])
#     elif my_lis[0]=='print':
#         print(empty_li)

#Captilize
name=input("Enter the Name: ")
cap_name=name.capitalize()
print(cap_name)



#...................list Comprehension ..................#
animals=['lion','frog','monkey','elephant','tigar']
filtered_animal=[]
for animal in animals:
    filtered_animal.append(animal.title())
print(filtered_animal)
 
filtered_animals=[animal2.title() for animal2 in animals] #list comprehension
print(filtered_animals) 

#........................tuples..............................#
#Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
n=int(input())
t=tuple(map(int,input().split()))
print(hash(t))

#Find a string
String=input()
sub_string=input()
start=0
end=len(sub_string)
counter=0
while start<=len(string)-end:
    if String[start:start+end]==sub_string:
        counter +=1
    start +=1
print(counter)