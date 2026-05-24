#simple login system using if else methods and logical opeartors
print("****Welcome to admin login page****")

correct_username = "Admin"
correct_password = "123456789"


user_name=input("Enter your username: ")
password=input("Enter your password: ")

if user_name == correct_username and password == correct_password:
    print("Successfully logged in")
    print("Welcome admin")
elif user_name != correct_username or password == correct_password:
    print("Invalid username")
    print("Try again")
elif user_name == correct_username or password != correct_password:
    print("Invalid password")
    print("Try again")
else:
    print("Access denied")