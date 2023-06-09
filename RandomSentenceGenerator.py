import random
import keyboard

dictionary = {
    "name":["Peter", "Michell", "Jane", "Steve"],
    "place": ["Sofia", "Plovdiv", "Varna", "Burgas"],
    "verb": ["eats", "holds", "sees", "plays with", "brings"],
    "noun": ["stones", "cake", "apple", "laptop", "bikes"],
    "adverb": ["slowly", "diligently", "warmly", "sadly", "rapidly"],
    "detail": ["near the river", "at home", "in the park"]
            }

def start():
    name = random.choice(dictionary["name"])
    place = random.choice(dictionary["place"])
    verb = random.choice(dictionary["verb"])
    noun = random.choice(dictionary["noun"])
    adverb = random.choice(dictionary["adverb"])
    detail = random.choice(dictionary["detail"])
    print(f"{name} from {place} {adverb} {verb} {noun} {detail}")
    print("Click [Enter] to generate a new one./[Esc] to end the program.")


print("\nTo edit lists use those commands:\n")
print("!check [list]/all\n!add [list] [element]\n\nTo start the generator use:\n!start")

command = input()
break_ = False
while True:
    command = command.split()
    if command[0] == "!check":
        if command[1] == "all":
            print(dictionary)
        else:
            print(dictionary[command[1]])
    elif command[0] == "!add":
        dictionary[command[1]].append(command[2])
    elif command[0] == "!start":
        start()
        while True:
            if keyboard.read_key() == "enter":
                start()
            if keyboard.read_key() == "esc":
                break_ = True
                break
    if break_ == True:
        break
    command = input()