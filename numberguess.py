import random
r=input("Please enter a number: ")
if r.isdigit():
    r=int(r)
    if r<=0:
        r=input("Please enter a number greater than 0: ")
else:
    r=input("Please enter a digit:" )
    
random_no=random.randrange(0,r)
guesses=0
while True:
    user_guess=input("Make a guess ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        if user_guess<=0:
            print("Please enter a number greater than 0: ")
    else:
        print("Please enter a digit:" )
        continue
    if user_guess==random_no:
        print("You got it!!")
        guesses=guesses+1
        break
    elif user_guess<random_no:
        print("You were below number")
        guesses=guesses+1
    elif user_guess>random_no:
        print("You were above the number")
        guesses=guesses+1
if(guesses>1):
    print("You got it in "+str(guesses)+" guesses")
else:
    print("Congrats!! You got it in "+str(guesses)+" guess")
    