import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range) 
    
if top_of_range <= 0:
    print('Please type a number larger than 0 next time.')
    quit() 

r = random.randint(0,top_of_range)
#print(r)

while True:
    user_guess = input("Make a guess: ")
   
    if user_guess.isdigit():
        user_guess = int(user_guess) 
    else:
        print('Please type a number next time.')
        continue

    if user_guess == r:
        print('you got it!')
        break
    else:
        print('you got it wrong')

