def test(long long value):
    cdef long long i
    cdef long long z
    for i in xrange(value):
        z = i**2
        if(i==1000000):
            print i
        if z < i:
            print "yes"
