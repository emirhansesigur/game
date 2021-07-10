print(".....Welcome to my game!......")

print("If you want to learn what the game is, please write 'what' ")
print("If you already know the game, please write something else")
a = input("").lower()
if a == "what":
    print("There are 5 questions about Turkey and we want you write to correct answer.")

playing = input("Do you want to play now? ")

if playing.lower() != "yes":
    quit()

print("Let's start :)")

print("You have 5 questions!")
    
score = 0

answer = input("1) Where is the capital of Turkey? ")

if answer.lower() == "ankara":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("2) What is Turkey's the most populous city? ")

if answer.lower() == "istanbul":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("3) How many cities are there in Turkey? ")

if answer == "81":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("4) What language is mainly spoken in Turkey? ").lower()

if answer == "turkish":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("5) What is the main religion in Turkey ").lower()

if answer == "islam":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")

print("...here are the answers...")
print("1) ankara")
print("2) istanbul")
print("3) 81")
print("4) turkish")
print("5) islam")
