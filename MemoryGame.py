import random, time
from Utils import screen_cleaner

def generate_sequence(difficulty):
    """
    This Method will generate sequence and return a list on items
    :param difficulty: user difficulty
    :return: list
    """
    mem_list = []
    for i in range(difficulty):
        mem_list.append(random.randint(1, 101))
    return mem_list

def get_list_from_user(difficulty):
    """
    This Method will get input from user and make a list of what user remember from the random list
    :param difficulty: user difficulty
    :return: list
    """
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter.")
    user_list = []
    for i in range(1, difficulty + 1):
        while True:
            try:
                user_input = int(input(f"please enter item number {i}: "))
            except ValueError as e:
                print(f"You Get a {e.__class__.__name__}\nplease enter only an integer number")
            if user_input > 101 or user_input < 0:
                print("please choose number between 1-101")
            else:
                user_list.append(user_input)
                break

    return user_list

def is_list_equal(list_a, list_b):
    """
    This Method will compare it see if our two lists are equal or not by check item by item,
    this means it will check if each item in same index is equal.

    :param list_a: first list
    :param list_b: second list
    :return: result if they equal it will return True, if not it will return False
    """
    result = True
    for x in list_a:
        for y in list_b:
            if x != y:
                result = False
            else:
                result = True
    return result


def play(difficulty):
    """
    This Method will Start the game.
    :param difficulty: user difficulty
    :return: True if user won or False if user lost
    """

    computer_mem_list = generate_sequence(difficulty)
    print(computer_mem_list)
    time.sleep(0.7)
    screen_cleaner()
    user_mem_list = get_list_from_user(difficulty)

    if is_list_equal(computer_mem_list, user_mem_list):
        return True
    else:
        return False
