class Library:

    def __init__(self, books):
        self.books = books

    def show_avail_books(self):
        print('Our Library Can Offer You The Following Books:')
        print('================================================')
        for book, borrower in self.books.items():
            if borrower == 'Free':
                print(book)

    def lend_book(self, requested_book, name):
        if self.books[requested_book] == 'Free':
            print(f'{requested_book} has been marked as \'Borrowed\' by: {name}')
            self.books[requested_book] = name
            return True
        else:
            print(f'Sorry, the {requested_book} is currently on loan to: {self.books[requested_book]}')
            return False

    def return_book(self, returned_book):
        self.books[returned_book] = 'Free'
        print(f'Thanks for returning {returned_book}')


class Student:
    def __init__(self, name, library):
        self.name = name
        self.books = []
        self.library = library

    def view_borrowed(self):
        if not self.books:
            print('You haven\'t borrowed any books')
        else:
            for book in self.books:
                print(book)

    def request_book(self):
        while True:
            try:
                book = input('Enter the name of the book you\'d like to borrow >> ')
                if book in self.library.books:
                    if self.library.lend_book(book, self.name):
                        self.books.append(book)
                        break
                    else:
                        continue
                else:
                    print('Book not found in the library. Please try again.')
            except Exception as e:
                print('An error occurred:', e)

    def return_book(self):
        while True:
            try:
                book = input('Enter the name of the book you\'d like to return >> ')
                if book in self.books:
                    self.library.return_book(book)
                    self.books.remove(book)
                    break
                else:
                    print('You haven\'t borrowed that book, try another...')
            except Exception as e:
                print('An error occurred:', e)


def create_lib():
    books = {
        'The Last Battle': 'Free',
        'The Hunger Games': 'Free',
        'Cracking the Coding Interview': 'Free',
        'Python Crash Course': 'Free',
        'Algorithms by Robert Sedgewick': 'Free',
        'Eloquent JavaScript': 'Free',
    }
    library = Library(books)
    student_example = Student('Your Name', library)

    while True:
        print('''
            ==========LIBRARY MENU===========
            1. Display Available Books
            2. Borrow a Book
            3. Return a Book
            4. View Your Books
            5. Exit''')

        try:
            choice = int(input('Enter Choice: '))
            if choice == 1:
                print()
                library.show_avail_books()
            elif choice == 2:
                print()
                student_example.request_book()
            elif choice == 3:
                print()
                student_example.return_book()
            elif choice == 4:
                print()
                student_example.view_borrowed()
            elif choice == 5:
                print('Goodbye')
                break
            else:
                print('Invalid choice. Please select a valid option.')
        except ValueError:
            print('Invalid choice. Please enter a numeric value.')

if __name__ == '__main__':
    create_lib()