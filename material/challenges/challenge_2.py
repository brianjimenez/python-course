import sys


class Atom(object):
    def __init__(self, atom_type):
        self.atom_type = atom_type


class Oxygen(Atom):
    def __init__(self):
        Atom.__init__(self, 'O')


class Hydrogen(Atom):
    def __init__(self):
        Atom.__init__(self, 'H')


class Water(object):
    def __init__(self, oxygen, hydrogen1, hydrogen2):
        self.oxygen = oxygen
        self.hydrogens = [hydrogen1, hydrogen2]


def usage():
    print "Usage: %s num_oxygen num_hydrogen" % sys.argv[0]

if __name__ == "__main__":
    try:
        num_oxygen = int(sys.argv[1])
        num_hydrogen = int(sys.argv[2])
    except:
        usage()
        raise SystemExit('Error in parameters')

    oxygens = [Oxygen() for _ in range(num_oxygen)]
    hydrogens = [Hydrogen() for _ in range(num_hydrogen)]

    waters = []
    hydrogen_counter = 0
    oxygen_counter = 0
    for oxygen in oxygens:
        if len(hydrogens) >= 2:
            waters.append(Water(oxygen, hydrogens[hydrogen_counter], hydrogens[hydrogen_counter + 1]))
            hydrogen_counter += 2
            oxygen_counter += 1
    
    print '%d water molecules created' % len(waters)
    print '%d oxygen remainder' % (len(oxygens) - oxygen_counter)
    print '%d hydrogen remainder' % (len(hydrogens) - hydrogen_counter)
