import random

COUNTER = 0

rules = str('''
==== The rules of game: ====
Guessed 4 numbers. You need to guess it.
You have 3 attempts.
In case if some number in your inputted NUMBER is correct and in correct position you will receive message BULLS.
In case if some number in your inputted NUMBER is correct but position is incorrect you will receive message COWS.
Good luck!
''')

print(rules)

#array_nums = []

number_one = str(random.randint(0, 9))
number_two = str(random.randint(0, 9))
number_three = str(random.randint(0, 9))
number_four = str(random.randint(0, 9))
number = int(number_one + number_two + number_three + number_four)

array_nums = (number_one, number_two, number_three, number_four)

print(array_nums)

guess_num = int(input("Your number is: "))

first_num = guess_num // 1000
second_num = guess_num // 100 % 10
third_num = guess_num // 10 % 10
fourth_num = guess_num % 10

if int(guess_num) == number:
	print(f"You win! correct is number is {array_nums}")
else:
	print(f" You lose :( Correct num is {number}")
