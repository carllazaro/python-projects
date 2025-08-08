import random
import time

def art2():
    print("█▀█ █▀█ █▀▀ █▄▀   █▀█ ▄▀█ █▀█ █▀▀ █▀█   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀")
    print("█▀▄ █▄█ █▄▄ █░█   █▀▀ █▀█ █▀▀ ██▄ █▀▄   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█")

def main():
    print("---Welcome to Rock, Paper, Scissor---")
    art2()

    while True:
        press_s = input("Press [s] to start: ").upper()
        if press_s == "S":
            for i in range(1, 6):
                print(f"\rLoading [{i*20}%]", end="")
                time.sleep(1)
            print(" ")
            start()
            break
        else:
            print("Press [s]")

def start():
    #Scores
    user = 0
    computer = 0

    while True:
        options = ["Rock", "Paper", "Scissor"]
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]

        print("\nPress [R] for Rock, [P] for Paper, [S] for Scissor, [Q] to Quit")
        option = input("> ").upper()

        #Quit
        if option == "Q":
            if user > computer:
                print(f"Score: ♛ User - {user} | Computer - {computer}")
                print("Thanks for playing!")
            elif user < computer:
                print(f"Score: User - {user} | Computer - {computer} ♛")
                print("Thanks for playing!")
            else:
                print(f"Score: User - {user} | Computer - {computer}")
                print("Thanks for playing!")
            break

        if option not in ['R', 'P', 'S']:
            print("Invalid input. Please choose [R], [P], [S], or [Q].")
            continue

        print(f"Computer chose: {computer_pick}")

        if option == "R":
            if computer_pick == "Scissor":
                print("You won!")
                user += 1
            elif computer_pick == "Paper":
                print("You lose")
                computer += 1
            else:
                print("It's a tie!")
        
        elif option == "P":
            if computer_pick == "Rock":
                print("You won!")
                user += 1
            elif computer_pick == "Scissor":
                print("You lose")
                computer += 1
            else:
                print("It's a tie!")
        
        elif option == "S":
            if computer_pick == "Paper":
                print("You won!")
                user += 1
            elif computer_pick == "Rock":
                print("You lose")
                computer += 1
            else:
                print("It's a tie!")

        print(f"Score: User - {user} | Computer - {computer}")
        print()
main()
