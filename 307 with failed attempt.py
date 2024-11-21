import time

MAX_LOGIN_ATTEMPTS = 3
LOCKOUT_DURATION = 10  # seconds

def login(username, password):
    # Simulating a database of user credentials
    users = {
        "user1": "password1",
        "user2": "password2",
        "user3": "password3"
    }

    if username in users and users[username] == password:
        return True
    else:
        return False

def main():
    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username, password):
            print("Login successful!")
            break
        else:
            attempts += 1
            print("Login failed. Attempts remaining:", MAX_LOGIN_ATTEMPTS - attempts)
            if attempts == MAX_LOGIN_ATTEMPTS:
                print("Too many login attempts. Try again after a while.")
                time.sleep(LOCKOUT_DURATION)
                attempts = 0

if __name__ == "__main__":
    main()
