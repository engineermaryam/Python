print(" Welcome to the Quiz Game...")
score = 0

choose = input(" Do you want to play this game? ")

if choose.lower() == "yes":
  print(" Okay, lets play!")
else:
  quit()

answer = input(" What is the capital of Pakistan? ")
if answer.lower() == "islamabad":
  print("Correct")
  score += 1
else:
  print("Incorrect")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("Correct")
  score += 1
else:
  print("Incorrect")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
  print("Correct")
  score += 1
else:
  print("Incorrect")

print(" You got " + str(score) + " questions correct")
print("You got " + str((score/3) * 100) + " %")
