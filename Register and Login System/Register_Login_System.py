#version 1.0.0
#made by carllazaro

import re
import calendar
import platform
import os
import sys
import time
import pwinput

#System art
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

def dashboard(): #dashboard where the user can select his/her option
    while True:
        print("[1] Login                                            [4] Version \n[2] Register                                         "
        "[5] System Status\n[3] About this project                               [6] Exit")
        try:
            select = int(input("> ")) #prompting user
            if select == 1: #will directly go to login section
                login()
                break
            elif select == 2: #will directly go to register section
                register()
                break
            elif select == 3: #about section
                about()
                exit_ = input("Exit [E]: ").upper()
                if exit_ == "E":
                    dashboard()
            elif select == 4: #version section 
                version()
                exit_ = input("Exit [E]: ").upper()
                if exit_ == "E":
                    dashboard()
            elif select == 5: #status of the system, user's machine
                system_status()
            elif select == 6: #will terminate the program
                exit()
            else:
                print("Invalid option!")
        except ValueError:
            print("Please enter a valid number.")

def get_environment_info(): #getting the user's machine info
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Python Version": platform.python_version(),
        "Architecture": platform.machine(),
        "Current Working Directory": os.getcwd(),
        "Platform": os.name,
    }
def system_status(): #displaying the machine's status two items per row
    items = list(get_environment_info().items())

    for i in range(0, len(items), 2):
        pair1 = f"{items[i][0]}: {items[i][1]}"

        if i + 1 < len(items):
            pair2 = f"{items[i + 1][0]}: {items[i + 1][1]}"
        else:
            pair2 = ""

        print(f"    {pair1:<40} {pair2}")

def version(): #version of the system including my github profile and as well as the repository for this system
    major_version = 1
    minor_version = 0
    patches = 0
    print(f"\x1B[3mVersion {major_version}.{minor_version}.{patches}\nstandby for updates on my github: https://github.com/carllazaro"
          "\nRepository: https://github.com/carllazaro/Python-Projects\x1B[0m")
def about(): #about this project (will expand this in the future)
    print("This project showcases a registration and login system, where the " \
    "program prompts the user to choose between registering [1] \nor logging in [2]. " \
    "The user can register with a unique username and password, which will be stored in " \
    "database.txt. Users can \nregister multiple accounts and access any of them by logging in.")
    
def register(): #register section, the user can register any username or password he/she wants, but it need to meet the conditions required
    special_characters = r"!@#$%^&*()-_+=\{\}[\]|\\:;\"'<>,.?/`~" #special characters for the username and password creation
    numbers = r"0123456789" #numbers in string form for the username and password creation

    username = input("\nUsername: ") #prompt the user for the username
    password = pwinput.pwinput(prompt="Password: ", mask="*") #password prompt

    # patterns for detection
    special_pattern = re.compile(f"[{re.escape(special_characters)}]")
    number_pattern = re.compile(f"[{re.escape(numbers)}]")

    # username checks
    username_has_special = bool(special_pattern.search(username))
    username_has_number = bool(number_pattern.search(username))

    # password checks
    password_has_special = bool(special_pattern.search(password))
    password_has_number = bool(number_pattern.search(password))

    valid = True #default
    #conditions that the username and password need to meet
    if not username_has_special:
        print("Username must contain at least one special character.")
        valid = False
    if not username_has_number:
        print("Username must contain at least one number.")
        valid = False

    if not password_has_special:
        print("Password must contain at least one special character.")
        valid = False
    if not password_has_number:
        print("Password must contain at least one number.")
        valid = False
    if valid: #if the username and password meet the conditions, then the account will be registered
        file_exists = os.path.exists("database.txt")
        is_empty = os.path.getsize("database.txt") == 0 if file_exists else True
        with open("database.txt", "a") as file:
            #this section will check if the file txt is empty, if empty, then the header will be printed 
            # along with the username and password 
            # if this header is not found, then it will be printed to the txt file
            if is_empty:
                file.write("REGISTERED ACCOUNTS\n") #header
                file.write("----------------------------------------\n")
            file.write(f"{username}   |   {password}\n") # "|" is the border between registered username and password
        
        print("Account registered!\n") #indicating that the account is registered
        dashboard()

    else:
        print("Please fix the above issues and try again.") #displaying that the issues need to be fixed
        register()

def login(): #login section where the user can log in his/her registered account
    username = input("\nUsername: ")
    password = pwinput.pwinput(prompt="Password: ", mask="*")

    try:
        with open("database.txt", "r") as file:
            users = file.readlines() #will read the lines in the txt file
    except FileNotFoundError:
        print("No registered users yet. Please register first.") #if no users registered, then the message in this exception will be printed
        return #returning the error

    for i in range(1, 6):
        print(f"\rLogging in [{i * 20}%]", end="") #this is loading animation
        time.sleep(1) # 1 second, can be modified
    print("\r\033[K", end="")

    user_lines = users[2:] if len(users) >= 3 else []

    for user in user_lines:
        if '|' not in user:
            continue
        #split
        stored_username, stored_password = re.split(r'\s*\|\s*', user.strip())
        if username == stored_username and password == stored_password:
            print("Login successful!\n")
            logged_in(username)
            return
    #if username or password is incorrect, this will be printed and will return to the dashbaord
    print("Invalid username or password.")
    dashboard() 

def logged_in(username): #displaying a green corresponds with the user's username
    print(f"Welcome, @{username}")

print(art) #print art and call dashboard function
dashboard()