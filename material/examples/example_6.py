def my_add(x, y):
    """Adds x and y.

    >>> my_add(2,3)
    5
    >>> my_add(5,-5)
    0
    """
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
