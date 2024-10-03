from book import Book

books = {}

def add_book():
    title = input("Enter the title of the book you would like to add: ")
    author = input("Enter the book's author: ")
    publication_date = input("Enter the publication date of the book: ")
    genre = input("Enter the genre of the book: ")


    new_book = Book(title, author, publication_date, genre)

    books[title] = new_book

    print(f"{title} had been added to the books database successfully.")


# borrow book and  book are not finished - come back to them.
def borrow_book():
    title = input("Enter the title of the book you would like to borrow: ")
    if title in books:
        book = books[title]
        if book.is_available():
            book.set_availability(False)
            print(f"You have borrowed '{book.get_title}'.")
        else:
            print(f"'{book.get_title()}' is currently unavailable.")
    else:
        print(f"{title} was not found in database.")



def return_book():
    title = input("Enter the title of the book you would like to return: ")
    if title in books:
        book = books[title]

        if not book.is_available():
            book.set_availability(True)
            print(f"'{book.get_title()}' has been returned successfully.")

        else:
            print("According to records, you have not borrowed this book.")

    else:
        print("The title entered was not found in the database.")


def search_book():
    title = input("Enter the title of the book you would like to search for: ")
    found = False
    for book in books.values():
        if book.get_title() == title:
            found = True
            print(f"'{book.get_title()}' was found in the database. Author: {book.get_author()}.")
            break
    if not found:
        print("The title you entered was not entered in the database.")


def display_books():
    if books:
        for book in books.values():
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, Genre: {book.get_genre()}, Available: {'Yes' if book.is_available() else 'No'}")

    else:
        print("The book database is currently empty.")
