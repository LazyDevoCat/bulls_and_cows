import random

number = str()

while len(number) != 4:
    new_num = str(random.randint(0, 9))
    if new_num in number:
        continue
    else:
        number = number + new_num


print(number)