def check_case(character):
    
    """Print whether the given single character is uppercase, lowercase,
    or not a letter at all."""

    if character.isupper():
        print(f"'{character}' is an UPPERCASE letter.")

    elif character.islower():
        print(f"'{character}' is a lowercase letter.")

    else:
        print(f"'{character}' is not a letter, so case does not apply.")


user_char = input("Enter a character: ")

check_case(user_char)