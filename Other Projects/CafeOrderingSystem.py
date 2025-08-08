def start():
    while True:
        print("---WELCOME---")
        print("[1] Menu")
        print("[2] Exit")
        select = input("> ")
        if select == "":
            print("Select something!")
        elif not select.isdigit():
            print("Select [1-3] only!")
        elif select == "1":
            Menu()
            break
        elif select == "2":
            quit()

def Menu():
    menu = ["Espresso", "Flat White", "Latte", "Tea",]
    while True:
        print("-----MENU-----")
        for coffee in menu:
            print(f"{[menu.index(coffee) + 1]} {coffee}")
        select = input("> ")
        if select == "":
            print("Select something!")
        elif not select.isdigit():
            print("Select [1-4] only!")
        elif select == "1":
            while True:
                confirm = input("Confirm Order? [Y/N]: ")
                if confirm == "Y":
                    print(f"Order confirmed ({menu[0]})")
                    quit()
                elif confirm == "N":
                    print("Order cancelled!")
                    Menu()
                    break
        elif select == "2":
            while True:
                confirm = input("Confirm Order? [Y/N]: ")
                if confirm == "Y":
                    print(f"Order confirmed ({menu[1]})")
                    quit()
                elif confirm == "N":
                    print("Order cancelled!")
                    Menu()
                    break
        elif select == "3":
            while True:
                confirm = input("Confirm Order? [Y/N]: ")
                if confirm == "Y":
                    print(f"Order confirmed ({menu[2]})")
                    quit()
                elif confirm == "N":
                    print("Order cancelled!")
                    Menu()
                    break
        elif select == "4":
            while True:
                confirm = input("Confirm Order? [Y/N]: ")
                if confirm == "Y":
                    print(f"Order confirmed ({menu[3]})")
                    quit()
                elif confirm == "N":
                    print("Order cancelled!")
                    Menu()
                    break
        else:
            print("Select [1-4] only!")
start()