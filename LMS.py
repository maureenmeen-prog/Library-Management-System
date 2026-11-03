books=[]
borrowed=[]
def add_books ():
    book=input("Enter book: ")
    books.append(book)
    print("book added")
def view_books ():
    for book in books:
        print(book)
def search_book ():
    book=input("Enter book: ")
    if book in books:
        print("book found")
    else:
        print("book not found")
def borrow_book ():
    book=input("Enter book: ")
    if book in books:
        books.remove(book)
        borrowed.append(book)
        print("book borrowed")
def return_book ():
    book=input("Enter book")
    if book in borrowed:
        borrowed.remove(book)
        books.append(book)
        print("book returned")
    else:
        print("book was not borrowed")
def delete_book ():
    book=input("Enter book: ")
    if book in books:
        books.remove(book)
        print("book deleted")
    else:
        print("book not found")
while True:
        print("~~ LIBRARY MANAGEMENT SYSTEM ~~")
        print("1.Add book")
        print("2.View books")
        print("3.Search book")
        print("4.Borrow book")
        print("5.Return book")
        print("6.Delete book")
        print("7.Thanks for visiting see you next time")
        choice=input("Enter a choice")
        if choice == "1":
            add_books()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("Thanks for visiting see you next time")
            break
        