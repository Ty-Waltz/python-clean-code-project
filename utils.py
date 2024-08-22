import re

def validate_input(pattern, prompt):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid input, please try again.")