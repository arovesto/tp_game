class Action:
    def __init__(self, specials=None):
        self.specials = specials

    def do_action(self, actor):
        pass


class WalkAction(Action):
    def do_action(self, actor):
        actor.world.move_entity(self.specials)


class AttackAction(Action):
    def do_action(self, actor):
        self.specials[0].attack(self.specials[1])
        actor.log("{} was attacked by {}".format(self.specials[1].name, self.specials[0].name))

