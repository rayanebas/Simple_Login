attempt = 3
while attempt > 0:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "password123":
        print("Login successful\nWelcome, admin!")
        break
    else:
        attempt -= 1
        print(
            f"Login failed\nInvalid username or password, please try again. Attempts left: {attempt}")
        if attempt == 0:
            print("Too many failed attempts. Please try again later.")
