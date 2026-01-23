import pdb;
pdb.set_trace()
print('''WELL COME TO LIBRARY!
        How can i help You? ''')
#Dummy data store 
Books={'001':{"title":'Python',
        "Author":'Guido van Roisum',
        "Availabilty_status":True
        }}
Member={'1':{
        "Name":'Ahmad',
        "Borrowed_books":[]
        }
}

#Adding New Book/Member
print('''Choice what user want:
         1.Add New Member
         2.Add New Book''')
choice_add=input("Enter Your adding choice")

if choice_add == '1':
  #add new member
  try:
    add_member_id=input("Enter New member id")
    member_name=input("Enter the name of Member: ")
    Member.update({add_member_id:{
         "Name":member_name,
          "Borrowed_books":[]
         }
     })
    print(f"Member successfully {Member}")
  except:
      print("Member not add.Try again")
elif choice_add =='2':
        try:
             add_book_id=input("Enter New Book id: ")
             add_author_name=input("Enter the name of Author:")
             Books.update({add_book_id:{"title":input("Enter the Title of Book: "),
             "Author":add_author_name,
             "Availabilty_status":True
              }})
             print(f"Book  successfully add{Books}")
        except:
                print("Book not Add Try")

print(f"Members of Library are: {Member}")

#USER WANT TO BORROWED/RETURN BOOKS#
print("Perform operations to Borrowed/Return Book")
member_id=input("Enter Member ID")
#Check condition for verification of member
if member_id in Member:
    print('''Select Choice!
          1.Borrowed Book
          2.Return Book''')
    #what Member want ? 
    choice=int(input())
    if choice==1:
        book_id=input("Enter Book id: ")
        if book_id in Books:
            if Books[book_id]['Availabilty_status']==True:
                Books[book_id]['Availabilty_status']=False
                Member[member_id]['Borrowed_books'].append(book_id)
                print(f"{book_id} borrowed book {Books}")
                print("Book Successfully borrowed")
            else:
                print("Book not available")
        else:
            print("Book not found")
    elif choice==2: #for return book 
        book_id=int(input("Enter Book_id: "))
        if Books[book_id]['Borrowed_books']:
                Member[member_id]['Borrowed_books'].remove(book_id)
                Books[book_id]['Availabilty_status']=True
                print(f"{member_id} return book {Books}")
                print("Book Successfully Return")
        else:
                print("Book not borrowed by You")
else:
  print('Member not Found')

  
  