import re
def dashboard():
    art = r'''
                                                        8
                                                        8
                                             .,,aadd88P=8=Y88bbaa,,.
                                       .,ad88888P:a8P:d888b:Y8a:Y88888ba,.
                                    ,ad888888P:a8888:a8888888a:8888a:Y888888ba,
                                 ,a8888888:d8888888:d888888888b:8888888b:8888888a,
                              ,a88888888:d88888888:d88888888888b:88888888b:88888888a,
                            ,d88888888:d888888888:d8888888888888b:888888888b:88888888b,
                          ,d88888888:d8888888888I:888888888888888:I8888888888b:88888888b,
                        ,d888888888:d88888888888:88888888888888888:88888888888b:888888888b,
                       d8888888888:I888888888888:88888888888888888:888888888888I:8888888888b
                      d8P"'   `"Y8:8P"'     `"Y8:8P"'    8    `"Y8:8P"'     `"Y8:8P"'   `"Y8b
                                                         8                                
                                                         8
                                                         8
                                                         8
                                                         8
                                                         8
                                                         8
                                                         8
                                                         8
                                                         8
                                                        ,8,
                                                        888
                                                        888      __
                                                        Y88b,,,d88P
                                                        `Y8888888P'
                                                          `"""""'
        '''

    print(art)

    while True:
        print("[1] Login\n[2] Register")
        try:
            select = int(input("> "))
            if select == 1:
                login()
                break
            elif select == 2:
                register()
                break
            else:
                print("Invalid option. Please choose 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")

def register():

    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
    '{', '[', '}', ']', '|', '\\', ':', ';', '"', "'", '<', ',', '>', '.', '?', '/', '`', '~']
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] #string numbers

    username = input("Username: ")
    password = input("Password: ")
    
    pattern = "[" + re.escape("".join(special_characters)) + "]"
    number ="[" + re.escape("".join(numbers)) + "]"
    match = re.search(pattern, username)
    match = re.search(pattern, password)
    match_number = re.search(number, username)
    match_number = re.search(number, password)
    
    if match and match_number:
        if username:
            with open("database.txt", "a") as file:
                file.write(f"{username},{password}\n")

            print("Account registered!")
            dashboard()
    else:
        print("Invalid username!")
        register()

def login():
    username = input("Username: ")
    password = input("Password: ")

    try:
        with open("database.txt", "r") as file:
            users = file.readlines()
    except FileNotFoundError:
        print("No registered users yet. Please register first.")
        return

    for user in users:
        stored_username, stored_password = user.strip().split(",", 1)
        if username == stored_username and password == stored_password:
            print("Login successful!")
            return

    print("Invalid username or password.")
    dashboard()

dashboard()