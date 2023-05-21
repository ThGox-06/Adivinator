from restart import restart


def checker_random_num(int_input_num, random_num):
    if int_input_num == random_num:
        print("You guessed it!")
    else:
        print(f"Wrong, the number is {random_num}")
