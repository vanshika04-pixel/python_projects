import random
user_wins=0
computer_wins=0
options= ["rock","paper","scissors"]
while True:
    user_input=input("Type Rock/Paper/Scissors or q to quit. ").lower()
    if user_input=='q':
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    #rock:0,paper:1,scissors:2
    computer_pick=options[random_number]
    print("Computer picked: ",computer_pick)
    if user_input=="rock" and computer_pick=="scissors":
        print("You win!")
        user_wins+=1
        continue
    elif user_input=="paper" and computer_pick=="rock":
        print("You won!")
        user_wins+=1
        continue
    elif user_input=="scissors" and computer_pick=="paper":
        user_wins+=1
        print("You win")
        continue
    elif user_input==computer_pick:
        print("Draw")
    else:
        print("Computer wins!")
        computer_wins+=1
print("Your score is: ",user_wins)
print("Computer's score is: ",computer_wins)
if(user_wins>computer_wins):
    print("Congrats!!You won"," by ",(user_wins-computer_wins)," points")
elif user_wins==computer_wins:
    print("Draw Match")
else:
    print("Computer wins by ",(computer_wins-user_wins)," points")
print("Goodbye")
    