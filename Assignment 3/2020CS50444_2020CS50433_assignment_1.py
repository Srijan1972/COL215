def is_legal_region(kmap_function, term):
    """
    Determines whether the specified region is LEGAL for the K-map function

    Parameters:
    kmap_function: n * m list containing the kmap function
        2-input kmap -> 2*2
        3-input kmap -> 2*4
        4-input kmap -> 4*4
    term: a list of size k, where k is the number of inputs in function
        term[i] = 0 | 1 | None

    Returns:
    Three-tuple: (top-left coordinate, bottom right coordinate, legality)
    """
    num = len(term)
    n = len(kmap_function)
    m = len(kmap_function[0])
    assert(2**num==n*m),"Kmap & term size do not match"
    legal = True
    tl = None
    br = None
    return (tl,br,legal)
    # your code here
