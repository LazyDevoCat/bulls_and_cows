import random


def generate_num():
    number = str()
    while len(number) != 4:
        new_num = str(random.randint(0, 9))
        if new_num in number:
            continue
        else:
            number = number + new_num
    return number


print(generate_num())


def check_player_input(number_from_player):
    try:
        int(number_from_player)
        if len(number_from_player) != 4:
            return "Write 4-digits"
        else:
            return number_from_player
    except ValueError:
        return "Write a number"


player_num = input("please write your number: ")
print(check_player_input(player_num))
