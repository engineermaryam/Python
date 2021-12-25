import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        elif comp == 'w':
            if you == 'g':
                return False
            elif you == 's':
                return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("Comp turn: Snake(s), Water(w), or Gun(g) ?")
randNo = random.randint(1, 3)
if randNo == 1:
     comp = 's'
elif randNo == 2:
     comp = '2'
elif randNo == 3:
     comp = '3'
you = input("Your turn: Snake(s), Water(w), Gun(g): ")
a = gameWin(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
     print("The game is a tie!")
elif a:
     print("You Win!")
else:
     print(" You Loose!")
