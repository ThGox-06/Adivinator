import random
from restart import restart
from checker_random_num import checker_random_num


def checker_10(int_input_num):
    random_num = random.randint(1, 10)
    if int_input_num > 10:
        print(f"{int_input_num} is greater than 10")
        return restart()
    else:
        checker_random_num(int_input_num, random_num)
        return restart()
