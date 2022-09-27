
class Armor(object):
    def __int__(self, name='Default', armor=0):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(armor, float)
        self.armor = armor

    def __str__(self):
        return 'name : {}, armor : {}'.format(self.name, self.armor)