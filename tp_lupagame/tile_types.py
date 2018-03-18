# Description of tile types in format of:
#   name : (walkability, transparency, possibility to penetrate, function that runs when someone go to tile)


def damage(hp):
    return lambda entity: entity.damage(hp)


def nothing(entity):
    pass

TilesTypes = {
    "dirt" : (True, True, True, "..", nothing),
    "wall" : (False, False, False, "▓▓", nothing),
    "trap" : (True, True, True, ",,", damage(3)),
}


TilesProbabilities = {
    "dirt" : 0.6,
    "wall" : 0.3,
    "trap" : 0.1,
}

SpecialTiles = {
    "exit" : (True, True, True, "[]", ""),
}