def restart():
    restarting = input("Do you want to continue? Y/N: ")
    return restarting.lower() in ("s", "si", "y", "yes")

