
from datetime import datetime
from re import sub
subtotal = float(input("What is the subtotal of this purchase? $"))
exacttime = datetime.now()
weekday = exacttime.weekday()
if subtotal >= 50:
    if weekday == 1 or weekday == 2:
        discount = subtotal * .1
        subtotal -= discount
        print(f"Discount: ${discount:.2f}.")
tax = subtotal * .06
total = subtotal + tax
print(f"Tax: ${tax:.2f}.")
print(f"Total: ${total:.2f}.")