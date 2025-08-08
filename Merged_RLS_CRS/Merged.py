#version 1.0.0
#made by carllazaro

import re
import calendar
import platform
import os
import sys
import time
import pwinput
import random
import datetime

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

start_dt = datetime.date(2025, 8, 1)
end_dt = datetime.date(2025, 12, 1)
time_between_dates = end_dt - start_dt
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_dt + datetime.timedelta(days=random_number_of_days)

print("Cinema Reservation System")
print("--------------------------")
movie = ["Fight Club", "Finding Nemo", "Oppenheimer"]
cities = ["Los Angeles", "Visakhapatnam", "New York City", "Mumbai", "Toronto", "Atlanta", "Berlin", "Las Vegas", "Manila"]
theater = ["IMDb", "IMAX", "4DX"]

random_showcase = random.randint(0, 2)
random_city = random.randint(0, 8)
random_theater = random.randint(0, 2)
# --------------------------------------------------------

def dashboardcinema():
    print("Returning to cinema dashboard...\n")

def ticketreservation():
    print("          TICKET RESERVATION\n")
    print("--------| EXIT |----------| EXIT |------")
    print("--------|      |----------|      |------\n")

    # === Setup: Seat matrix and random reserved seats (only ONCE) ===
    seat_matrix = [[1, 2, 3, 4, 5, 6],
                   [7, 8, 9, 10, 11, 12],
                   [13, 14, 15, 16, 17, 18],
                   [19, 20, 21, 22, 23, 24],
                   [25, 26, 27, 28, 29, 30]]
    
    screen = ['S','C', 'R', 'E', 'E', 'N']

    # Randomly reserve 6–10 seats (marked as ' R')
    reserved_count = random.randint(6, 10)
    reserved_positions = set()
    while len(reserved_positions) < reserved_count:
        row = random.randint(0, 4)
        col = random.randint(0, 5)
        reserved_positions.add((row, col))

    for row, col in reserved_positions:
        seat_matrix[row][col] = ' R'

    # === Loop interaction until user confirms ===
    while True:
        # Display seating layout
        print("  ", end="|")
        for i in range(len(seat_matrix[0])):
            print(f"C{i+1} ", end="|")
        print("      |  S")

        for i, row in enumerate(seat_matrix, start=1):
            print(f"R{i}", end="|")
            for item in row:
                print(f"{item:2} ", end="|")
            print(f"      |  {screen[i]}")

        print("\n--------| EXIT |----------| EXIT |------")
        print("--------|      |----------|      |------")

        # Ask for seat selection
        while True:
            seat_reserve = input("Select a seat (e.g., R2C3): ").upper().strip()

            try:
                if not (seat_reserve.startswith('R') and 'C' in seat_reserve):
                    raise ValueError

                r_index = seat_reserve.index('R') + 1
                c_index = seat_reserve.index('C')

                seat_row = int(seat_reserve[r_index:c_index]) - 1
                seat_col = int(seat_reserve[c_index+1:]) - 1

                if not (0 <= seat_row <= 4 and 0 <= seat_col <= 5):
                    print("Invalid seat number. Please choose between R1C1 to R5C6.\n")
                    continue

                if seat_matrix[seat_row][seat_col] == ' R':
                    print("Seat already reserved by another customer. Please choose another seat.\n")
                elif seat_matrix[seat_row][seat_col] == ' *':
                    print("You've already selected this seat.\n")
                else:
                    seat_matrix[seat_row][seat_col] = ' *'
                    break
            except:
                print("Invalid format. Use format like R2C3 (no space)\n")

        # Theater availability
        available_theaters = {}
        print("\nSelect theater:")

        for t in theater:
            available_theaters[t] = random.choice([True, False])

        while True:
            for i, t in enumerate(theater, start=1):
                status = "Available" if available_theaters[t] else "Not Available"
                print(f"[{i}] {t} - {status}")

            try:
                choice = int(input("Enter theater number: "))
                if 1 <= choice <= len(theater):
                    selected = theater[choice - 1]
                    if available_theaters[selected]:
                        print(f"{selected} selected.\n")
                        break
                    else:
                        print("That theater is not available. Please choose another one.\n")
                else:
                    print("Invalid input. Please choose a valid number.\n")
            except ValueError:
                print("Invalid input. Enter a number.\n")

        # Seat pricing based on column
        if seat_col in [0, 1]:
            print("C1-C2: Regular seats")
        elif seat_col in [2, 3]:
            print("C3-C4: VIP seats")
        elif seat_col in [4, 5]:
            print("C5-C6: Premium regular seats")

        # Ask for confirmation
        while True:
            confirm = input("Confirm reservation [Y/N]: ").upper()
            if confirm == "Y":
                print("Reservation confirmed. Thank you!\n")
                return  # End function
            elif confirm == "N":
                print("Reservation cancelled. Please choose again...\n")
                # Remove previously selected seat before retrying
                seat_matrix[seat_row][seat_col] = (seat_row * 6 + seat_col + 1)
                break  # Go back to the beginning of the loop
            else:
                print("Invalid input. Please enter Y or N.")

#AFTER CONFIRMATION, NEED MAPUNTA SA DASHBOARD TAPOS NAKALAGAY FLASH YUNG NIRESERVE NA TICKET AT SEAT
#KAILANGAN DIN IINDICATE NUNG USER YUNG MOVIE NA PANONOORIN AT YUNG DATE NA NAKA BASE DUN SA SHOWING

def dashboardcinema():
    print(f"Movie: {movie[random_showcase]}")
    if random_showcase == 0:
        print(f"Theater: {theater[random_theater]}")
        print(f"City: {cities[random_city]}")
        print(f"Date: {random_date}")
    if random_showcase == 1:
        print(f"Theater: {theater[random_theater]}")
        print(f"City: {cities[random_city]}")
        print(f"Date: {random_date}")
    if random_showcase == 2:
        print(f"Theater: {theater[random_theater]}")
        print(f"City: {cities[random_city]}")
        print(f"Date: {random_date}")
    
    print("--------------------------")
    select = ["Reserve a Ticket", "Movies", "Theaters", "Trailers", "Events & Promos", "Logout"]
    for selection_index in select:
        print(f"[{select.index(selection_index) + 1}] {selection_index}")
    while True:
        pick = input("> ")
        match pick:
            case "1":
                ticketreservation()
            case "2":
                print("Movies")
            case "3":
                print("Cinemas")
            case "4":
                print("Trailers")
            case "5":
                print("Events & Promos")
            case "6":
                for i in range(1, 6):
                    print(f"\rLogging out [{i * 20}%]", end="") #this is loading animation
                    time.sleep(1) # 1 second, can be modified
                print("\r\033[K", end="")
                print("Account Logged out!\n")
                dashboard()

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
    print(f"Welcome, @{username}\n")
    dashboardcinema()
print(art) #print art and call dashboard function

dashboard()
