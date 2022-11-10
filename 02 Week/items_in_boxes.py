import math
items = int(input("Enter the number of items: "))
per = int(input("Enter the number of items per box: "))
boxes = math.ceil(items / per)
print(f"\nFor {items} items, packing {per} items in each box, you will need {boxes} boxes.")
