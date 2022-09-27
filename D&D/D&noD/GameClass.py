
from PlayerClass import *
from InventoryClass import *

if __name__ == '__main__':
    weapon_test = Weapon(name='BAM')
    inventory_test = Inventory(weapon_test)
    player_test = Player(inventory=inventory_test)


    print(player_test)
    player_test.addHeal(10.0)
    print(player_test)
