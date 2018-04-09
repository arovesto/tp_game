from utill.singleton import Singleton
from utill.geometry import Circle


class Data:

    def __init__(self, mobs, map):
        self.mobs = mobs
        self.map = map


class MoveDisposer(Singleton):

    def __init__(self, game):
        self.game = game

    def is_in_sight(self, observed):
        return observed

    def make_move(self, entity):
        in_sight = self.is_in_sight(Circle(entity.radius_of_visibility, entity.position))
        map = {}
        mobs = {}
        for p in in_sight:
            if p in self.game.world.map:
                map[p] = self.game.world.map[p]
            if p in self.game.world.mobs:
                mobs[p] = self.game.world.mobs[p]
        action = entity.move(Data(mobs, map))
        self.handle_action(action)

    def handle_action(self, action):
        action.do_action(self.game)
