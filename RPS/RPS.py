import random

user_score = 0 
computer_wins = 0 

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == 'q':
        break
        
    if user_input not in ["rock", "paper", "scissors"]:
        continue
    random_number = random.randint(0,2)
    # rock = 0, paper = 1 sciossrs =  2


print("Goodbye!")
        
