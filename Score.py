import Utils
import os

def add_score(points):
    """
    this Method will update user score and print the score
    :param points: the points user get from the level
    :return: None
    """
    score_file_source = Utils.SCORES_FILE_NAME

    if os.path.exists(score_file_source):
        score_file_txt = open(score_file_source, 'r+')
        score_file_txt.write(str(points))
    else:
        score_file_txt = open(score_file_source, 'w')
        score_file_txt.write(str(points))

    print(f"Your Score is {points}")
