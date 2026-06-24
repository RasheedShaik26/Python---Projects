class library:
    def __init__(self):
        self.noBooks = 0                # ---it is constructor
        self.books = []

    def addBook( self , book):
        self.books.append(book)              # --- this method is used to addbooks
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f" the library has {self.noBooks} books . the books are")       # --- this is used to show the information of the book
        for book in self.books:
             print(book)


l1 = library()
l1.addBook("harry potter 1:")
l1.addBook("harry poter 2:")
l1.addBook("harry poter 3:")

l1.showInfo()