import random

def generate_number(difficulty):
        """
        This Method will get a difficulty and generate random number from 1 to difficulty.
        :param difficulty: user level choice
        :return: generated number from random module
        """
        gen_num = random.randint(1, difficulty)
        return gen_num

def get_guess_from_user(difficulty):
    """
    This method will get user guess number.
    :param difficulty: user level choice
    :return: user guess number
    """
    while True:
        try:
            user_guess_num = int(input("please enter your guess number: "))
        except ValueError as e:
            print(f"You Get a {e.__class__.__name__}\nplease enter only an integer number")
            continue

        if user_guess_num < 1 or user_guess_num > difficulty:
            print(f'please choose number between 1 to {difficulty}')
        else:
            break
    return user_guess_num

def compare_results(difficulty, secret_number):
    """
    This method will compare user guess number to random number ot see if user right or wrong.
    :param difficulty: user level choice
    :param secret_number: the number who user suppose guess
    :return:
    """
    user_guess = get_guess_from_user(difficulty)

    if user_guess == secret_number:
        return True
    else:
        return False

def play(difficulty):
    """
    This method will play the Guess Game
    :param difficulty: user level choice
    :return: if user won or lose
    """
    secret_num = generate_number(difficulty)
    result = compare_results(difficulty, secret_num)

    return result