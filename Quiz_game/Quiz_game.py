print("Welcome to my computer quiz!")
score = 0
playing = input("Do you want to play? ")

if playing != "yes":
    quit()
    
print("Okay! Lets play :)")

answer = input("What does cpu stand for? ")

if answer == "central processing unit":
    print("CORRECT!")
    score += 1
else: 
    print("INCORRECT!")
    
print("your score is", score)