""" Python code to implement classes and objects """

from urllib import response


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def display_info(self):
        print("User Details: ")
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Password: ", self.password)

    def user_registration():
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in user_db:
            if user.email == email:
                print("DB: ", user_db)
                print(email)
                print("User already exists")
                return

        new_user = User(name, email, password)
        user_db.append(new_user)
        print("User created successfully")

user_db = []

while True:
    User.user_registration()
    response = input("Do you want to continue? (Enter 'skip' to stop): ")
    if response.lower() == 'skip':
        break
