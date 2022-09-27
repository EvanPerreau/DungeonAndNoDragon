
from InventoryClass import *


class Player(object):

    ####################
    #       INIT       #
    ####################

    def __init__(self, name='Joueur 1', health=100.0, attack_damage=0.0, armor=0.0, inventory=Inventory):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(health, float)
        self.health = health
        assert isinstance(attack_damage, float)
        self.attack_damage = attack_damage
        assert isinstance(armor, float)
        self.armor = armor
        assert isinstance(inventory, object)
        self.inventory = inventory

    ####################
    #       STR        #
    ####################

    def __str__(self):
        return 'name : {},\n health : {},\n attack_damage : {},\n armor : {},\n inventory : {}\n'.format(self.name, self.health,
                                                                                               self.attack_damage,
                                                                                               self.armor,
                                                                                               self.inventory)

    ####################
    #      SETTER      #
    ####################

    def setName(self, name):
        assert isinstance(name, str)
        self.name = name
        return

    def addHeal(self, amount):
        assert isinstance(amount, float)
        self.health += amount
        return

    def subtractHeal(self, amount):
        assert isinstance(amount, float)
        self.health -= amount
        return

    def setHeal(self, amount):
        assert isinstance(amount, float)
        self.health = amount
        return

    def addAttackDamage(self, amount):
        assert isinstance(amount, float)
        self.attack_damage += amount
        return

    def subtractAttackDamage(self, amount):
        assert isinstance(amount, float)
        self.attack_damage -= amount
        return

    def setAttackDamage(self, amount):
        assert isinstance(amount, float)
        self.attack_damage = amount
        return

    def addArmor(self, amount):
        assert isinstance(amount, float)
        self.armor += amount
        return

    def subtractArmor(self, amount):
        assert isinstance(amount, float)
        self.armor -= amount
        return

    def setArmor(self, amount):
        assert isinstance(amount, float)
        self.armor -= amount
        return

    def setInventory(self, inventory):
        assert isinstance(inventory, object)
        self.inventory = inventory
