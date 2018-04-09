from utill.action import Action


def get_action(beginning_phrase=""):
    print(beginning_phrase)
    phrase = input().split()
    return Action(phrase[0], phrase[1:])


def get_start_info():
    print("What is your name")
    return input()


def format_to_resolution(raw, resolution=(10, 20)):
    for i in range(resolution[0]):
        for j in range(resolution[1]):
            print(raw[(i, j)])