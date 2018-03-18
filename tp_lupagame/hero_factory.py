from hero_types import HeroTypes


class HeroFactory:
    @staticmethod
    def create_hero(self, kind, position):
        hero = HeroTypes(kind)(position)
        return hero

