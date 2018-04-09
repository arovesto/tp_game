import random

from maping.tile import Tile
from maping.tile_types import TilesTypes, TilesProbabilities
from utill.singleton import Singleton


class TileFactory(Singleton):
    @staticmethod
    def random_tile(self):
        tile = Tile()
        tile.name = random.choices(TilesProbabilities.keys(), TilesProbabilities.values())
        tile.walkable, tile.transparent, tile.penetrable, tile.look, tile.on_step = TilesTypes[tile.name]
