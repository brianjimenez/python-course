from random import randrange
import sys


class Dinosaur(object):
    def __init__(self, size):
        self.size = size

    def roar(self):
        pass


class TyrannosaurusRex(Dinosaur):
    def __init__(self, size):
        Dinosaur.__init__(self, size)
        self.name = 'Tyrannosaurus Rex'

    def roar(self):
        return 'WROOOooooOOaaarrr!'


class Triceratops(Dinosaur):
    def __init__(self, size):
        Dinosaur.__init__(self, size)
        self.name = 'Triceratops'

    def roar(self):
        return 'buff! buff!'


class JurassicPark(object):
    """Represents the Jurassic Park from the famous movie"""

    def __init__(self):
        """Creates a Jurassic Park"""
        self._tyrannosaurus = []
        self._triceratops = []

    def add_trex(self, trex):
        self._tyrannosaurus.append(trex)

    def add_triceratops(self, tri):
        self._triceratops.append(tri)

    def battle(self):
        for trex in self._tyrannosaurus:
            print 'A %s (%d): %s' % (trex.name, trex.size, trex.roar())
        for tri in self._triceratops:
            print 'A %s (%d): %s' % (tri.name, tri.size, tri.roar())
        
        num_trex = len(self._tyrannosaurus)
        num_tri = len(self._triceratops)

        if num_trex <= 0 or num_tri <= 0:
            print 'No battle is possible. Peace.'
            return

        if num_trex > num_tri / 2.:
            print 'Tyrannosaurus killed the triceratops herd'
            self._triceratops = []
        else:
            if sum([dinosaur.size for dinosaur in self._tyrannosaurus]) < sum([dinosaur.size for dinosaur in self._triceratops]):
                print 'Triceratops killed one tyrannosaurus!'
                try:
                    del self._tyrannosaurus[-1]
                except IndexError:
                    pass
            else:
                print 'Battle finishes OK'


def usage():
    print "Usage: %s num_carnivores num_herbivores" % sys.argv[0]


if __name__ == "__main__":
    """The park simulation"""    
    try:
        num_carnivores = int(sys.argv[1])
        num_herbivores = int(sys.argv[2])
    except:
        usage()
        raise SystemExit('Wrong command line')

    park = JurassicPark()
    for _ in range(num_carnivores):
        park.add_trex(TyrannosaurusRex(randrange(5, 15)))

    for _ in range(num_herbivores):
        park.add_triceratops(Triceratops(randrange(7, 10)))

    park.battle()
    

