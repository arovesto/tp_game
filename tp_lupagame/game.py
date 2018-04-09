from world import World
from utill.log import Log


class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.world = World()
        self.log = Log()

    def is_over(self):
        return len(self.world.find_mobs_by(lambda mob: mob.factor == "computer")) == 0

    def render(self):
        return self.world.showed_tiles()

    def make_move(self, action):
        pass     # validate action and do it if possible

    def result(self):
        pass  # returns string for showing end of game
