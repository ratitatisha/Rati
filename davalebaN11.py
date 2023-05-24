def count_characters():
    user_input = input("What is the input string? ")

    if user_input:
        character_count = len(user_input)
        print(f"{user_input} has {character_count} characters.")
    else:
        print("You must enter something.")

count_characters()
