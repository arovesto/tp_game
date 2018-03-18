import random

from geometry import distance


class Direction:
    @staticmethod
    def move_up(position):
        return position[0] - 1, position[1]

    @staticmethod
    def move_down(position):
        return position[0] + 1, position[1]

    @staticmethod
    def move_left(position):
        return position[0], position[1] - 1

    @staticmethod
    def move_right(position):
        return position[0], position[1] + 1

    @staticmethod
    def possible_moves(position):
        return (
            Direction.move_up(position),
            Direction.move_down(position),
            Direction.move_left(position),
            Direction.move_right(position),
        )

    @staticmethod
    def move_towards(self, from_position, to_position):
        return list(sorted(Direction.possible_moves(from_position), key=lambda x: distance(x, to_position), reverse=True))

    @staticmethod
    def filtered_possible_moves(position, filter_fun):
        return list(filter(filter_fun, Direction.possible_moves(position)))


