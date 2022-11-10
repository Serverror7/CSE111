import random
stars = random.randrange(100,300,3)
while stars >= 0:
	if stars == 0:
		break
	else:
		stars -= 1
		print(stars)