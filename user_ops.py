from user import User

users = {}

def add_user():
    name = input("Enter your first and last name: ")
    library_ID = input("Enter your library ID: ")
    new_user = User(name, library_ID)
    users[library_ID] = new_user
    print(f"'{name}' has been added to the User database successfully.")

def view_user_details():
    library_ID = input("Enter the Library ID of the user you would like to view: ")
    if library_ID in users:
        user = users[library_ID]
        print(f"User details: Name: {user.get_name()}, Library ID: {user.get_library_ID()}")
    else:
        print("User not found in database.")

def display_users():
    if users:
        for user in users.values():
            print(f"Name: {user.get_name()}, Library ID: {user.get_library_ID()}")
    else:
        print("User database is currently empty.")
