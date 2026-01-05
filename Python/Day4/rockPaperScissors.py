import random

rock = r'''                       
                                            88         
                                            88         
                                            88         
            8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
            88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
            88         8b       d8 8b         8888[      
            88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
            88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a'''

paper = r''' 
             _        _ _      _                               
            | |      (_) |    | |                              
            | |_ ___  _| | ___| |_ _ __   __ _ _ __   ___ _ __ 
            | __/ _ \| | |/ _ \ __| '_ \ / _` | '_ \ / _ \ '__|
            | || (_) | | |  __/ |_| |_) | (_| | |_) |  __/ |   
            \__\___/|_|_|\___|\__| .__/ \__,_| .__/ \___|_|   
                                | |         | |              
                                |_|         |_|              '''

scissors = r'''  
                 ____
                / __ \
                ( (__) |___ ___
                \________,'   """""----....____
                _______<  () dd       ____----'
                / __   __`.___-----""""
                ( (__) |
                \____/
'''

art = [rock, paper, scissors]
user_input = input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: ")

if user_input not in ["0", "1", "2"]:
    win = -1
    user_choice = -1
else:
    user_choice = int(user_input)
cpu_choice = random.randint(0, 2)

if user_choice != -1:
    if user_choice == cpu_choice:
        win = 3
    elif user_choice == 0:
        if cpu_choice == 1:
            win = 0
        else: 
            win = 1
    elif user_choice == 1:
        if cpu_choice == 2:
            win = 0
        else: 
            win = 1
    elif user_choice == 2:
        if cpu_choice == 0:
            win = 0
        else: 
            win = 1


if win == -1:
    print("Invalid choice by the user. Try Again!!")
else:
    print("You choose:\n")
    print(art[user_choice])
    print("\nAI choose:\n")
    print(art[cpu_choice])

    if win == 0:
        print("\nAI wins!")
    elif win == 3:
        print("\nIt's a Draw.")
    else:
        print("\nYou win!!")