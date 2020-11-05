def welcome(name):
    """
    This method is a Welcome Message for user.
    :param name: username
    :return: hello message
    """
    return f'Hello {name} and welcome to the World of Games (WoG)\nHere you can find many cool games to play.'

def load_game():
    """
    this method is a load game who user like to play.
    :return:
    """
    game_msg_menu = "Please choose a game to play:\n\t" \
                  "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n\t" \
                  "2. Guess Game - guess a number and see if you chose like the computer"
    game_msg_level = "Please choose game level from 1-5: "
    print(game_msg_menu)
    while True:
        try:
            user_game_choice = int(input("please choose: "))
            break
        except ValueError as e:
            print(f"You Get a {e.__class__.__name__}\nplease enter only an integer number")

    while True:
        if user_game_choice == 1 or user_game_choice == 2:
            break
        else:
            print(game_msg_menu)
            try:
                user_game_choice = int(input("your choice is not exists, please choose agein: "))
            except ValueError as e:
                print(f"You Get a {e.__class__.__name__}\nplease enter only an integer number")

    while True:
        try:
            user_level_choice = int(input(game_msg_level))
        except ValueError as e:
            print(f"You Get a {e.__class__.__name__}\nplease enter only an integer number")
        if user_level_choice < 1 or user_level_choice > 5:
            print("out of range, please choose again")
        else:
            break
    return user_game_choice, user_level_choice