import random

from singleton import Singleton
from mob_types import MobTypes


class MobFactory(Singleton):
    @staticmethod
    def random_mob(self, position):
        return MobTypes[random.choice[MobTypes]](position)

    @staticmethod
    def by_name(self, name, position):
        return MobTypes[name](position)