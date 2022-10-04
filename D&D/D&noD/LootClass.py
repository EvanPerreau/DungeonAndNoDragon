
from WeaponClass import *
from ArmorClass import *
from PotionClass import *


class Loot(object):
    """créer un loot avec une arme, une arumre et une potion"""
    
    def __int__(self, name='Default', weapon=Weapon, armor=Armor, potion=Potion):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(weapon, object)
        self.weapon = weapon
        assert isinstance(armor, object)
        self.armor = armor
        assert isinstance(potion, object)
        self.potion = potion
