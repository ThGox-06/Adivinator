from checker_natural import checker_natural
from introduction import header

# Header
header("Adivinator")
# Checker
swapper = True
while swapper:
    input_num = input("Tell me a natural number between 1 and 10: ")
    swapper = checker_natural(input_num)
