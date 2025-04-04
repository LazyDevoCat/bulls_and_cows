import random

COUNTER = 0

rules = str('''
==== The rules of game: ====
Guessed 4 numbers. You need to guess it.
You have 3 attempts.
In case if some number in your inputted NUMBER is correct and in correct position you will receive message BULLS.
In case if some number in your inputted NUMBER is correct but position is incorrect you will receive message COWS.
HINT: first number couldn't be 0.
Good luck!
''')

print(rules)

number_one = str(random.randint(1, 9))
number_two = str(random.randint(0, 9))
number_three = str(random.randint(0, 9))
number_four = str(random.randint(0, 9))
number = str(number_one + number_two + number_three + number_four)

# print(number)

player_num = str(input("Your number is: "))


def compare(number_from_player: str, known_number: str):
	BULL = 0
	COWS = 0
	for number in range(len(known_number)):
		if number_from_player[number] == known_number[number]:
			BULL = BULL + 1
		if number_from_player[number] in known_number and number_from_player[number] != known_number[number]:
			COWS = COWS + 1
	print(f"BULL is {BULL} and COWS is {COWS}")


print(compare(player_num, number))



