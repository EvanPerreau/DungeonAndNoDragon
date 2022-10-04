
from LootClass import *


class Chest(object):
    """créer un coffre avec un nom, un loot, et si il est piégé"""
    
    def __init__(self, name='Default', loot=Loot, trap=False):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(loot, object)
        self.loot = loot
        assert isinstance(trap, bool)
        self.trap = trap

    def __str__(self):
        return 'name: {}, loot : {}, trap : {}'.format(self.name, self.loot, self.trap)
