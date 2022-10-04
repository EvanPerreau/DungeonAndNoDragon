
class Weapon(object):
    """créer une arme avec un nom et des points d'attaque"""
    
    def __init__(self, name='Default', attack_damage=0.0):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(attack_damage, float)
        self.attack_damage = attack_damage

    def __str__(self):
        return 'name : {}, attack_damage : {}'.format(self.name, self.attack_damage)
