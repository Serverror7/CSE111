import math
from datetime import datetime
time = datetime.now()
pi = math.pi
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the tire in inches (ex 15): "))
v = ((pi * (w ** 2) * ( a *(w * a + 2540 * d)))/10000000000)

print(f"The approximate volume is {v:.4} liters")

pnumber = str(input("Would you like to buy tires with these dimensions? Yes/No "))
if pnumber.strip("., !?-").lower() == "yes":
    number = input("What is your phone number? ")

with open("volumes.txt", "at") as volumes:
    print(f"{time:%Y-%m-%d}, {w}, {a}, {d}, {v:.4}, #{number}", file=volumes)
