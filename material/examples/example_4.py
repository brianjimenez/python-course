class Dinosaur(object):
    """Represents a dinosaur"""
    def __init__(self, name, era='Cretaceous'):
        self.name = name
        self.era = era

    def eat(self):
        pass


class TyrannosaurusRex(Dinosaur):
    """A super carnivore dinosaur"""
    def __init__(self):
        Dinosaur.__init__(self, 'Tyrannosaurus Rex')

    def eat(self):
        print 'I am carnivore'


trex = TyrannosaurusRex()
trex.eat()
