from maping.tile_factory import TileFactory


class Map:

    def __init__(self, map_size):
        self.width, self.height = map_size
        self.tiles = self.create_tiles()

    def __getitem__(self, item):
        return self.tiles[item]

    def create_tiles(self):
        return {(i, j) : TileFactory.random_tile() for i in range(self.width) for j in range(self.height)}
