""" Python code to implement classes and objects """

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
        user_db = []

        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in user_db:
            if user.email == email:
                print("User already exists")
                return

        new_user = User(name, email, password)
        user_db.append(new_user)
        print("User created successfully")

new_user = User.user_registration()
