import random

from tile import Tile
from tile_types import TilesTypes, TilesProbabilities
from singleton import Singleton


class TileFactory(Singleton):
    @staticmethod
    def random_tile(self):
        tile = Tile()
        tile.name = random.choices(TilesProbabilities.keys(), TilesProbabilities.values())
        tile.walkable, tile.transparent, tile.penetrable, tile.look, tile.on_step = TilesTypes[tile.name]
