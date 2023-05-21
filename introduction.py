def header(title):
    print("ThGox-06\nV 1.0")
    terminal_width = 80  # Desired width for header
    spliter = "=" * terminal_width

    # Print the top spliter
    print(spliter)

    # Print title centered
    spaces = (terminal_width - len(title)) // 2
    formatted_title = f"{spaces * ' '}{title}{spaces * ' '}"
    print(formatted_title)

    # Print bottom spliter
    print(spliter)
