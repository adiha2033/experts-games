import os

def screen_cleaner():
    """
    This Method will clear the screen.
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = "Something went wrong.."

