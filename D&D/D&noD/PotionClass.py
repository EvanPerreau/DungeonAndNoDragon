
class Potion(object):
    """définit une potion avec un nom, une augmentation de points de vie et une augmentation de points de dégats"""
    
    def __int__(self, name='Default', heal=False, damage=False):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(heal, bool)
        self.heal = heal
        assert isinstance(damage, bool)
        self.damage = damage

    def __str__(self):
        return 'name : {}, heal : {}, damage : {}'.format(self.name, self.heal, self.damage)
