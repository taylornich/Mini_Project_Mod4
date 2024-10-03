from author import Author

authors = {}

def add_author():
    author_name = input("Enter the name of the author you would like to add: ")
    biography = input("Enter a short biography for the author: ")

    new_author = Author(author_name, biography)
    authors[author_name] = new_author

    print(f"{new_author} has been added to Authors successfully.")


def view_author():
    author_name = input("Enter the name of the author you would like to view: ")

    if author_name in authors:
        author = authors[author_name]
        print(f"{author.get_author()}, Biography: {author.get_biography()}")

    else:
        print("Author not found.")


def display_authors():
    if authors:
        for author in authors.values():
            print(f"Name: {author.get_author()}, Biography: {author.get_biography()}")
    else:
        print("Author database is empty.")
