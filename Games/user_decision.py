def get_user_decision(prompt):
    user_input = input(prompt).lower()
    if user_input in ('y', '', 'yes'):
        return True
    elif user_input in ('n', 'no'):
        return False
    else:
        print("Your input is not recognized!!! Pls try again")
        return get_user_decision(prompt)