from restart import restart
from checker_10 import checker_10


def checker_natural(input_num):
    list_input_num = list(input_num)
    for i in list_input_num:
        ascii_i = ord(i)
        if not 48 <= ascii_i <= 57:
            print("The number isn't natural")
            return restart()

    int_input_num = int(input_num)
    return checker_10(int_input_num)

