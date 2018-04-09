import random

from utill.singleton import Singleton
from maping.map import Map
from units.mobs.mob_factory import MobFactory
from units.mobs.mob_types import MobLooks
from maping.tile_types import TilesTypes


class World(Singleton):
    def __init__(self, map_size = (100, 100), mobs_amount = 100):
        self.map = Map(map_size)
        self.mobs = self.create_mobs(mobs_amount)

    def create_mobs(self, mobs_amount):
        position = (random.randint(self.map.width), random.randint(self.map.height))
        return {position : MobFactory.random_mob(position) for _ in range(mobs_amount)}

    def showed_tiles(self):
        return {p: MobLooks[self.mobs[p].type] for p in self.mobs}.update({p: TilesTypes[self.map[p].type][3] for p in self.map.tiles})

    def find_mobs_by(self, filter_func):
        return list(filter(filter_func, (a for a in self.mobs.values())))
