print("Welcome to my Computer quiz!")
playing=input("Do you want to play the game? ")
if playing.lower()!="yes":
    quit()
print("Okay let's play then :)")
score=0
ans=input("What does cpu stand for? ")
if ans.lower()=="central processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect!")
    
ans=input("what does gpu stand for? ")
if ans.lower()=="graphics processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect!")
ans=input("what does ram stand for? ")
if ans.lower()=="random access memory":
    print("correct!")
    score+=1
else:
    print("incorrect!")
    
ans=input("what does psu stand for? ")
if ans.lower()=="power supply":
    print("correct!")
    score+=1
else:
    print("incorrect!")
print("You got "+format(score)+" questions correct!")
print("So your score is "+str((score/4)*100))