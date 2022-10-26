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
    m = len(kmap_function)
    n = len(kmap_function[0])
    assert(2**num==n*m),"Kmap & term size do not match"
    legal = True
    tlx = 0
    tly = 0
    brx = 0
    bry = 0
    if num==2:
        a = term[0]
        b = term[1]
        if a is None:
            tlx = 0
            brx = 1
        elif a==0:
            tlx = 0
            brx = 0
        else:
            tlx = 1
            brx = 1
        if b is None:
            tly = 0
            bry = 1
        elif b==0:
            tly = 0
            bry = 0
        else:
            tly = 1
            bry = 1
    elif num==3:
        a = term[0]
        b = term[1]
        c = term[2]
        if c is None:
            tly = 0
            bry = 1
        elif c==0:
            tly = 0
            bry = 0
        else:
            tly = 1
            bry = 1
        if a is None:
            if b is None:
                tlx = 0
                brx = 3
            elif b==0:
                tlx = 3
                brx = 0
            else:
                tlx = 1
                brx = 2
        elif a==0:
            if b is None:
                tlx = 0
                brx = 1
            elif b==0:
                tlx = 0
                brx = 0
            else:
                tlx = 1
                brx = 1
        else:
            if b is None:
                tlx = 2
                brx = 3
            elif b==0:
                tlx = 3
                brx = 3
            else:
                tlx = 2
                brx = 2   
    elif num==4:
        a = term[0]
        b = term[1]
        c = term[2]
        d = term[3]
        if c is None:
            if d is None:
                tly = 0
                bry = 3
            elif d==0:
                tly = 3
                bry = 0
            else:
                tly = 1
                bry = 2
        elif c==0:
            if d is None:
                tly = 0
                bry = 1
            elif d==0:
                tly = 0
                bry = 0
            else:
                tly = 1
                bry = 1
        else:
            if d is None:
                tly = 2
                bry = 3
            elif d==0:
                tly = 3
                bry = 3
            else:
                tly = 2
                bry = 2
        if a is None:
            if b is None:
                tlx = 0
                brx = 3
            elif b==0:
                tlx = 3
                brx = 0
            else:
                tlx = 1
                brx = 2
        elif a==0:
            if b is None:
                tlx = 0
                brx = 1
            elif b==0:
                tlx = 0
                brx = 0
            else:
                tlx = 1
                brx = 1
        else:
            if b is None:
                tlx = 2
                brx = 3
            elif b==0:
                tlx = 3
                brx = 3
            else:
                tlx = 2
                brx = 2
    else:
        print("Only supports kmaps of length 2,3 or 4")
        return ((tlx,tly),(brx,bry),legal)
    if tly>bry:
        for j in range(tly,m):
            if brx<tlx:
                for i in range(tlx,n):
                    if kmap_function[j][i]==0:
                        legal = False
                for i in range(0,brx+1):
                    if kmap_function[j][i]==0:
                        legal = False
            else:
                for i in range(tlx,brx+1):
                    if kmap_function[j][i]==0:
                        legal = False
        for j in range(0,bry+1):
            if brx<tlx:
                for i in range(tlx,n):
                    if kmap_function[j][i]==0:
                        legal = False
                for i in range(0,brx+1):
                    if kmap_function[j][i]==0:
                        legal = False
            else:
                for i in range(tlx,brx+1):
                    if kmap_function[j][i]==0:
                        legal = False
    else:
        for j in range(tly,bry+1):
            if brx<tlx:
                for i in range(tlx,n):
                    # print(j,i)
                    if kmap_function[j][i]==0:
                        legal = False
                for i in range(0,brx+1):
                    # print(j,i)
                    if kmap_function[j][i]==0:
                        legal = False
            else:
                for i in range(tlx,brx+1):
                    if kmap_function[j][i]==0:
                        legal = False
    return ((tlx,tly),(brx,bry),legal)
