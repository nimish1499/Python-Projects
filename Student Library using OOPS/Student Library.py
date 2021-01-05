class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present in the Library are: ")
        for book in self.books:
            print("\t", book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f'The book {bookName} has been issued to you. Keep it safe and return it within 30 days')
            self.books.remove(bookName)
            return True
        else:
            print('The Following book is either unvavailable or already issued to someone else, please wait until it '
                  'is available ')
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print('Thanks for returning the book')


class Student:
    def requestBook(self):
        self.book = input("Enter the book you would like to be Issued: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book you would like to Return: ")


if __name__ == '__main__':
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
    while True:
        a = int(input("Welcome to The Central Library \n 1. List Available Books \n "
                      "2. For Book Issue \n"
                      " 3. ""Return/Add of Book "
                      "\n 4. Exit the Library \n"))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for using the Library")
            exit()
        else:
            print("Invalid Choice")
