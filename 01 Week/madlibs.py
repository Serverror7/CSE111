strip = " .,!?"
print("Please enter the following: \n")
adjective1 = input("adjective: ")
adjective1 = adjective1.strip(strip)
animal1 = input("animal: ")
animal1 = animal1.strip(strip)
verb1 = input("verb: ")
verb1 = verb1.strip(strip)
exclamation1 = input("exclamation: ")
exclamation1 = exclamation1.strip(strip)
exclamation1 = exclamation1.capitalize()
exclamation2 = input("exclamation: ")
exclamation2 = exclamation2.strip(strip)
exclamation2 = exclamation2.capitalize()
verb2 = input("verb: ")
verb2 = verb2.strip(strip)
noun1 = input("place noun: ")
noun1 = noun1.strip(strip)
verb3 = input("verb: ")
verb3 = verb3.strip(strip)

print(f"\nYour story is:\n\nThe other day, I was really in trouble. It all started when I saw a very {adjective1} {animal1} {verb1} down the hallway. \"{exclamation1}!\" I yelled. I ran to the door, which was locked. All I could think to do was to yell \"{exclamation2}!\" while {verb2}ing over and over. Miraculously, that caused it to stop in {noun1}, but not before it tried to {verb3} right in front of my family.")