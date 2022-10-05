def is_legal_region(kmap_function, term):
    """
    determines whether the specified region is LEGAL for the K-map function
    Arguments:
    kmap_function: n * m list containing the kmap function
    for 2-input kmap this will 2*2
    3-input kmap this will 2*4
    4-input kmap this will 4*4
    term: a list of size k, where k is the number of inputs in function (2,3 or 4)
    (term[i] = 0 or 1 or None, corresponding to the i-th variable)
    Return:
    three-tuple: (top-left coordinate, bottom right coordinate, boolean value)
    each coordinate is represented as a 2-tuple
    """
    # your code here
