from units.mobs.mob import Mob
from utill.geometry import distance, can_move_to
from utill.action import AttackAction, Action, WalkAction
from utill.direction import Direction


class Warrior(Mob):

    max_hp = 100
    hp = 100
    speed = 3
    radius_of_visibility = 7
    damage = 20

    def __init__(self, position):
        self.position = position

    def move(self, observed_data):
        nearest_player_position = min((a for a in observed_data.mobs if observed_data.mobs[a].factor == "player"),
                                      lambda x: distance(observed_data[x].position, self.position), "no player nearby")
        if distance(nearest_player_position, self.position):
            return AttackAction((self, observed_data[nearest_player_position]))
        if nearest_player_position == "no player nearby":
            return Action()
        wanna_walk = Direction.move_towards(self.position, nearest_player_position)
        for p in wanna_walk:
            if can_move_to(observed_data)(p):
                return WalkAction((self, p))
        return Action("wait")
