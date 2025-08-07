import random
import datetime

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

def ticketreservation():
    print("          TICKET RESERVATION\n")
    print("--------| EXIT |----------| EXIT |------")
    print("--------|      |----------|      |------\n")
    seat_matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]]
    screen = ['S','C', 'R', 'E', 'E', 'N']
    print("  ", end="|")
    for i in range(len(seat_matrix[0])):
        print(f"C{i+1} ", end="|")
    print("      |  S")

    for i, row in enumerate(seat_matrix, start=1):
        print(f"R{i}", end="|")
        for item in row:
            print(f"{item:2} ", end="|")
        print(f"      |  {screen[i]}")
        #print("      |  C")
    
    print("\n--------| EXIT |----------| EXIT |------")
    print("--------|      |----------|      |------")

    seat_reserve = input("> ")
    print(" ")

    seat_reserve_row = int(seat_reserve[1]) - 1
    seat_reserve_column = int(seat_reserve[3]) - 1 

    seat_matrix[seat_reserve_row][seat_reserve_column] = ' *'

    print("  ", end="|")
    for i in range(len(seat_matrix[0])):
        print(f"C{i+1} ", end="|")
    print("      |  S")

    for i, row in enumerate(seat_matrix, start=1):
        print(f"R{i}", end="|")
        for item in row:
            print(f"{item:2} ", end="|")
        print(f"      |  {screen[i]}")
        #print("      |  C")
    
    print("\n--------| EXIT |----------| EXIT |------")
    print("--------|      |----------|      |------")
    print("Select theater: ")
    #AVAILABILITY ISSUE
    while True:
        for theater_count in theater:
            print(f"[{theater.index(theater_count) + 1}] {theater_count}", "Available" if random.getrandbits(1) else "Not Available")
        if seat_reserve_column in [0, 1]: #C1-C2: Regular price seats
            print("C1-C2")
            confirm = input("Confirm reservation [Y/N]: ").upper()
            if confirm == "Y":
                print("Reservation confirmed. Thank you!\n")
                dashboard()
                break
            elif confirm == "N":
                ticketreservation()
                break
            else:
                continue
            
        elif seat_reserve_column in [2, 3]: #C3-C4: High price seats/VIP
            print("C3-C4")
            confirm = input("Confirm reservation [Y/N]: ").upper()
            if confirm == "Y":
                print("Reservation confirmed. Thank you!\n")
                dashboard()
                break
            elif confirm == "N":
                ticketreservation()
                break
            else:
                continue
                
        elif seat_reserve_column in [4, 5]: #C5-C6: Regular but a little bit close to the price of C3-C4 seats
            print("C5-C6")
            confirm = input("Confirm reservation [Y/N]: ").upper()
            if confirm == "Y":
                print("Reservation confirmed. Thank you!\n")
                dashboard()
                break
            elif confirm == "N":
                ticketreservation()
                break
            else:
                continue
#AFTER CONFIRMATION, NEED MAPUNTA SA DASHBOARD TAPOS NAKALAGAY FLASH YUNG NIRESERVE NA TICKET AT SEAT
#KAILANGAN DIN IINDICATE NUNG USER YUNG MOVIE NA PANONOORIN AT YUNG DATE NA NAKA BASE DUN SA SHOWING

def dashboard():
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
    select = ["Reserve a Ticket", "Movies", "Cinemas", "Trailers", "Events & Promos"]
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
dashboard()
