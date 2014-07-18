
class Monster(object):
    """Represents a mythological creature"""

    latin_name = 'monstrum'

    def __init__(self, origin):
        self.origin = origin

    @classmethod
    def get_latin(cls):
        return cls.latin_name

    @staticmethod
    def battle(monster1, monster2):
        print 'A monster from %s is fighting a \
second monster from %s' % (monster1.origin, monster2.origin)

print Monster.get_latin()
kraken = Monster('Scandinavia')
print kraken.get_latin()
print kraken.get_latin
leviathan = Monster('Ancient Middle East')
Monster.battle(kraken, leviathan)
