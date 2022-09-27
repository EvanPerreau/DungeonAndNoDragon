
from ChestClass import *
from MonsterClass import *


class Room(object):
    def __init__(self, name='Default', chest=Chest, monster=Monster):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(chest, object)
        self.chest = chest
        assert isinstance(monster, object)
        self.monster = monster

    def __str__(self):
        return 'name : {},\n chest : {},\n monster : {}'.format(self.name, self.chest, self.monster)
