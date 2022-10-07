
from LootClass import *


class Monster(object):
    """créer un monstre avec un nom, des points de vie et d'attaques ainsi que un loot"""
    
    def __init__(self, name='Default', health=50.0, attack_damage=5.0, loot=Loot):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(health, float)
        self.health = health
        assert isinstance(attack_damage, float)
        self.attack_damage = attack_damage
        assert isinstance(loot, object)
        self.loot = loot

    def __str__(self):
        return 'name : {}, health : {}, attack_damage : {},\n loot : {}'.format(self.name, self.health,
                                                                              self.attack_damage, self.loot)
