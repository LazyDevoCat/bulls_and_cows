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


guessed_number = generate_num()
print(guessed_number)


def check_player_input(number_from_player):
    try:
        int(number_from_player)
        if len(number_from_player) != 4:
            return "Write 4-digits"
        else:
            checking = set()
            for num in number_from_player:
                checking.add(num)
            if len(checking) != 4:
                return "Write number without the same nums!"
            else:
                return number_from_player

    except ValueError:
        return "Write a number"


player_num = input("please write your number: ")
print(check_player_input(player_num))


def counting_cows_and_bulls(comp_number, player_number):
    cow_counter = 0
    bull_counter = 0
    for number in comp_number:
        if number in player_number:
            cow_counter = cow_counter + 1
            if player_number.rindex(number) == comp_number.rindex(number):
                bull_counter = bull_counter + 1
    return f"So you have {cow_counter} cow(s) and {bull_counter} buuul(s)!"


print(counting_cows_and_bulls(guessed_number, player_num))
