
from WeaponClass import *
from ArmorClass import *
from PotionClass import *


class Inventory(object):
    def __init__(self, weapon=Weapon, armor=Armor, potion=Potion):
        assert isinstance(weapon, object)
        self.weapon = weapon
        assert isinstance(armor, object)
        self.armor = armor
        assert isinstance(potion, object)
        self.potion = potion

    def __str__(self):
        return '\n weapon : {},\n armor : {},\n potion : {}'.format(self.weapon, self.armor, self.potion)
