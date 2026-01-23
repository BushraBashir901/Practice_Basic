import pdb;
pdb.set_trace()
class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_available=True
        
    def borrow(self): #Access is controlled using borrow() and return_book(), which is encapsulation in OOP.
        if self.is_available==True:
            self.is_available=False
            return True #if book borrowed then return TRUE
        return False #if book not borrowed then return False
    
    def return_book(self): 
        if self.is_available==False:
            self.is_available=True
b=Book(1,'python','ali')
a=b.borrow()
print(a)

class Member:
    def __init__(self,member_id,name):
        self.member_id=member_id
        self.name=name
        self.borrowed_books=[] #Attributes Track books borrowed
        
    def borrow_book(self,book_id):
        self.borrowed_books.append(book_id) #add book into borrowed list who's id is this
        
    def borrow_return(self,book_id):
        self.borrowed_books.remove(book_id) #Remove book into list who's id is this
m=Member(1,'Ayesha')
mm=m.borrow_book(1)
print(mm)
        
#---------------CLASS FOR PERFORMING OPERATIONS-------------#
class Library:  #Aggregation uses because library have objects of member and book classes object
    def __init__(self):
        self.add_books={}
        self.add_members={}
    def add_new_member(self,member_id,name):
        self.add_members[member_id]=Member(member_id,name)  #this is class of library but we use Member object in it
        print("Member Successfully Register")
        print(self.add_members)
    def add_new_book(self,book_id,title,author):
        self.add_books[book_id]=Book(book_id,title,author) #class of library but we use Book object in Library class
        store=self.add_books[book_id]
        print(f"store:{store}")
        print("Book Successfully Added")
                   #-----Borrow Book from dictionary-------------#
    def borrow_book(self,member_id,book_id):
        if member_id not in self.add_members:
            print("Member not Found in Records")
            return
        
        if book_id not in self.add_books:
            print("Books not Found")
            return
        
        book = self.add_books[book_id] #Accessing books add in dictionary 
        member = self.add_members[member_id] #Accessing Members add in dictionary 

        if book.borrow():
            member.borrow_book(book_id)
            print("Book borrowed successfully")
        else:
            print("Book not available")
            
    # Return book
    def borrow_return(self, member_id, book_id):
        if member_id not in self.add_members:
            print("Member not found")
            return

        member = self.add_members[member_id] #Accessing Members in dictionary 

        if book_id in member.borrow_book:
            member.return_book(book_id)
            self.add_books[book_id].borrow_return()
            print("Book returned successfully")
        else:
            print("This book was not borrowed by you")

    def show_Books(self):
        for book in self.add_books.values():
            if book.is_available==True:
                status='Available'
            else:
                status='Not Available'
            print(f"{book.book_id},{book.title},{status}")
            
    def show_members(self):
        for member in self.add_members.values():
            print(f"{member.member_id},{member.name},{member.borrow_book}")
    

# ---------- Operation performed here  ----------
library = Library() #object created-> Library class
print("WELCOME TO LIBRARY SYSTEM")

while True:
    print("""
1. Add Book
2. Add Member
3. Borrow Book
4. Return Book
5. View Books
6. View Member
7. Exit
""")
    choice = input("Enter choice: ")

    if choice == "1":
        b_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        library.add_new_book(b_id, title, author)

    elif choice == "2":
        m_id = input("Member ID: ")
        name = input("Member Name: ")
        library.add_new_member(m_id, name)

    elif choice == "3":
        m_id = input("Member ID: ")
        b_id = input("Book ID: ")
        library.borrow_book(m_id, b_id)

    elif choice == "4":
        m_id = input("Member ID: ")
        b_id = input("Book ID: ")
        library.borrow_return(m_id, b_id)
        
    elif choice == "5":
        library.show_Books()
        
    elif choice == "6":
        library.show_members()
           
    elif choice == "7":
        print("Thank you for using Library System")
        break

    else:
        print("Invalid choice")


