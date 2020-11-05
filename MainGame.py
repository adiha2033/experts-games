from Live import welcome, load_game
from Score import add_score

print(welcome("Adi"))
game, level = load_game()

if game == 1:
    import MemoryGame

    game_res = MemoryGame.play(level)

    if game_res == True:
        add_score(points=level)
        print("You Won")
    else:
        print("You Lost")

elif game == 2:
    import GuessGame
    game_res = GuessGame.play(level)

    if game_res == True:
        add_score(points=level)
        print("You Won")
    else:
        print("You Lost")