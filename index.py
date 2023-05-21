from checker_natural import checker_natural
from introduction import header

# Header
header("Adivinator")
# Checker
swaper = True
while swaper:
    input_num = input("Tell me a natural number between 1 and 10: ")
    swaper = checker_natural(input_num)
