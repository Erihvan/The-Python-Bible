import random

health = 50

difficulty = 1

"when you change difficulty, you divide potion health so the bigger the difficulty, the lower the health."
"you use int funtion to make a number from float or decimal into an integer or whole number"

potion_health = int(random.randint(25,50) / difficulty)

health = health + potion_health

print(health)
