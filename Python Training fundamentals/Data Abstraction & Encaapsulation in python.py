# Data Encapsulation & Abstraction :

class library:
    def __init__(self,books):
        self.books = books
    def listbooks(self):
        print("Available books :- ")
        for book in self.books:
            print(book)
    def borrowbook(self,borrowbook):
        if borrowbook in self.books:
            print("get your book ")
            self.books.remove(borrowbook)
        else:
            print("that book was not available")

    def receivebook(self):
        print("you have received a book .")
        self.books.append("receivebook")
            

books = ["python","java","javascript"]

b = library(books)

msg = '''
1.display book
2.borrow book
3.return book '''

while True :
    print(msg)
    ch = int (input("enter your choice : "))
    if ch == 1:
        b.listbooks()
    elif ch ==2 :
        book = input("enter book name to Borrow :")
        b.borrowbook(book)
    elif ch ==3 :
        book = input("enter book name to Return :")
        b.receivebook(book)
    else:
        print("thank you come again")
        quit()
    
