print("Welcome to my game")

playing = input("Do you wan to play? ")

if playing.lower() != "yes":
    quit()
    
print("Ok! Let's play: )")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")
   
answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    score += 1
    print('Correct!')
    
else: 
    print("Incorrect!")
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    score += 1
    print('Correct!')
else: 
    print("Incorrect!") 
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    score += 1
    print('Correct!')
else: 
    print("Incorrect!")   
    
print("You got " + str(score) + " questions correct")
print("You got " + str((score/4) * 100) + " %.")