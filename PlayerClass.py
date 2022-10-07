
from InventoryClass import *


class Player(object):
    """créer le joueur"""

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
        """change le nom du joueur"""
        assert isinstance(name, str)
        self.name = name
        return

    def addHeal(self, amount):
        """ajoute de la vie au joueur"""
        assert isinstance(amount, float)
        self.health += amount
        return

    def subtractHeal(self, amount):
        """enlève de la vie au joueur"""
        assert isinstance(amount, float)
        self.health -= amount
        return

    def setHeal(self, amount):
        """défini les points de vie du joueur"""
        assert isinstance(amount, float)
        self.health = amount
        return

    def addAttackDamage(self, amount):
        """Ajoute des points d'attaque au joueur"""
        assert isinstance(amount, float)
        self.attack_damage += amount
        return

    def subtractAttackDamage(self, amount):
        """réduit les points d'attaque du joueur"""
        assert isinstance(amount, float)
        self.attack_damage -= amount
        return

    def setAttackDamage(self, amount):
        """définit les points d'attaque du joueur"""
        assert isinstance(amount, float)
        self.attack_damage = amount
        return

    def addArmor(self, amount):
        """ajoute des points d'armure au joueur"""
        assert isinstance(amount, float)
        self.armor += amount
        return

    def subtractArmor(self, amount):
        """retire des points d'armure au joueur"""
        assert isinstance(amount, float)
        self.armor -= amount
        return

    def setArmor(self, amount):
        """définit les points d'armure du joueur"""
        assert isinstance(amount, float)
        self.armor = amount
        return

    def setInventory(self, inventory):
        """définit l'inventaire du joueur"""
        assert isinstance(inventory, object)
        self.inventory = inventory
