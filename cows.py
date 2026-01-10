"""This is main file with all logic"""
import random


def generate_num():
    """
    Generate 4digits number without replaying number inside
    """
    number = str()
    while len(number) != 4:
        new_num = str(random.randint(0, 9))
        if new_num in number:
            continue
        number = number + new_num
    return number


def check_player_input(number_from_player):
    """
    Checking player input
    """
    try:
        int(number_from_player)
        if len(number_from_player) != 4:
            return "Write 4-digits"
        checking = set()
        for num in number_from_player:
            checking.add(num)
        if len(checking) != 4:
            return "Write number without the same nums!"
        return number_from_player
    except ValueError:
        return "Write a number"


def counting_cows_and_bulls(comp_number, player_number):
    """
    Main logic of whole program
    """
    cow_counter = 0
    bull_counter = 0
    for number in comp_number:
        if number in player_number:
            if player_number.index(number) == comp_number.index(number):
                bull_counter += 1
            else:
                cow_counter += 1
    return f"So you have {cow_counter} cow(s) and {bull_counter} buuul(s)!"


def attempts_for_input():
    """
    Give 3 attempts for player
    """
    wrong_inputs = 3
    while wrong_inputs > 0:
        user_input = input("Enter a 4-digit number: ")
        result = check_player_input(user_input)
        if result == user_input:
            return user_input
        print(f"Error: {result}")
        wrong_inputs = wrong_inputs - 1
        print(f"Attempts left: {wrong_inputs}")
    if wrong_inputs == 0:
        return "Too many invalid attempts."


def rules():
    """
    Return just rules
    """
    return """Hello! You are running nano-game called "bulls and cows" Please read these rules:
    1) Guess 4-digit
    number awhere all digits are different.
    2) You have 3 attempts to guess number. And you will receive some tips.
    3) BULL - in your digit correct index and correct number (ex: your num 1253 guessed num is 4958 -> one bull
    number 5)
    4) COW - your digit is only correct number (ex: your num 1253 guessed is 2987 -> 1 cow number 2)
    """


def attempts():
    """
    Call two functions
    attempts_for_input
    and
    counting_cows_and_bulls
    """
    attempts = 0
    while attempts < 3:
        user_input = attempts_for_input()
        print(counting_cows_and_bulls(guessed_number, user_input))
        attempts = attempts + 1


print(rules())

guessed_number = generate_num()
print(guessed_number)


# user_input = attempts_for_input()
# print(counting_cows_and_bulls(guessed_number, user_input))

attempts()
