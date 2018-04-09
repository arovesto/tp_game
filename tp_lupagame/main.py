from game import Game
from utill.io import get_action, get_start_info, format_to_resolution


def main():
    print("Добро пожаловать в мою таверну")
    name = get_start_info()
    game = Game(name)
    while not game.is_over():
        move = get_action("Что хотите сделать? ")
        game.make_move(move)
        print(format_to_resolution(game.render()))
    print(game.result())


main()
