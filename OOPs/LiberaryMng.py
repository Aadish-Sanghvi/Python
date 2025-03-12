class Liberary:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def show_info(self):
        print(f"The liberary has {self.no_of_books} books.\n")

    def show_books(self):
        print("liberary has following books:")
        for i in self.books:
            print(i)

l1 = Liberary()
l1.addBook("The king of war")
l1.addBook("Rich dad poor dad")
l1.show_info()
l1.show_books()