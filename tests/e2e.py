from selenium import webdriver
import sys

def test_scores_service(app_url):
    """
    this method will get flask application url and check scores.
    :param app_url: http url
    :return: True or False
    """
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get(app_url)
    driver.implicitly_wait(15)
    score = driver.find_element_by_id("score").text
    score = int(score)

    driver.close()
    #if score < 1000 and score > 0:
    #    return True
    #else:
    #    return False
    return False

def main():
     if test_scores_service("http://localhost:8777"):
         return sys.exit(0)
     else:
         return sys.exit(1)

if __name__ == "__main__":
    main()



