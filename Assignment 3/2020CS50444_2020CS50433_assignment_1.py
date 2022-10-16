from K_map_gui_tk import *

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
    tlx = 0
    tly = 0
    brx = 0
    bry = 0
    if num==2:
        a = term[0]
        b = term[1]
        if a is None:
            tly = 0
            bry = 1
        elif a==0:
            tly = 0
            bry = 0
        else:
            tly = 1
            bry = 1
        if b is None:
            tlx = 0
            brx = 1
        elif b==0:
            tlx = 0
            brx = 0
        else:
            tlx = 1
            brx = 1
    elif num==3:
        a = term[0]
        b = term[1]
        c = term[2]
        if c is None:
            tlx = 0
            brx = 1
        elif c==0:
            tlx = 0
            brx = 0
        else:
            tlx = 1
            brx = 1
        if a is None:
            if b is None:
                tly = 0
                bry = 3
            elif b==0:
                tly = 3
                bry = 0
            else:
                tly = 1
                bry = 2
        elif a==0:
            if b is None:
                tly = 0
                bry = 1
            elif b==0:
                tly = 0
                bry = 0
            else:
                tly = 1
                bry = 1
        else:
            if b is None:
                tly = 2
                bry = 3
            elif b==0:
                tly = 3
                bry = 3
            else:
                tly = 2
                bry = 2   
    elif num==4:
        a = term[0]
        b = term[1]
        c = term[2]
        d = term[3]
        if c is None:
            if d is None:
                tlx = 0
                brx = 3
            elif d==0:
                tlx = 3
                brx = 0
            else:
                tlx = 1
                brx = 2
        elif c==0:
            if d is None:
                tlx = 0
                brx = 1
            elif d==0:
                tlx = 0
                brx = 0
            else:
                tlx = 1
                brx = 1
        else:
            if d is None:
                tlx = 2
                brx = 3
            elif d==0:
                tlx = 3
                brx = 3
            else:
                tlx = 2
                brx = 2
        if a is None:
            if b is None:
                tly = 0
                bry = 3
            elif b==0:
                tly = 3
                bry = 0
            else:
                tly = 1
                bry = 2
        elif a==0:
            if b is None:
                tly = 0
                bry = 1
            elif b==0:
                tly = 0
                bry = 0
            else:
                tly = 1
                bry = 1
        else:
            if b is None:
                tly = 2
                bry = 3
            elif b==0:
                tly = 3
                bry = 3
            else:
                tly = 2
                bry = 2
    else:
        print("Only supports kmaps of length 2,3 or 4")
        return ((tlx,tly),(brx,bry),legal)
    if tly>bry:
        for j in range(tly,n):
            if brx<tlx:
                for i in range(tlx,m):
                    if kmap_function[i][j]==0:
                        legal = False
                for i in range(0,brx+1):
                    if kmap_function[i][j]==0:
                        legal = False
            else:
                for i in range(tlx,brx+1):
                    if kmap_function[i][j]==0:
                        legal = False
        for j in range(0,bry+1):
            if brx<tlx:
                for i in range(tlx,n):
                    if kmap_function[i][j]==0:
                        legal = False
                for i in range(0,brx+1):
                    if kmap_function[i][j]==0:
                        legal = False
            else:
                for i in range(tlx,brx+1):
                    if kmap_function[i][j]==0:
                        legal = False
    else:
        for j in range(tly,bry+1):
            if brx<tlx:
                for i in range(tlx,m):
                    # print(j,i)
                    if kmap_function[i][j]==0:
                        legal = False
                for i in range(0,brx+1):
                    # print(j,i)
                    if kmap_function[i][j]==0:
                        legal = False
            else:
                for i in range(tlx,brx+1):
                    if kmap_function[i][j]==0:
                        legal = False
    # for highlighting region
    # kMap = kmap(kmap_function)
    # if legal:
    #     kMap.draw_region(tlx,tly,brx,bry,'green')
    # else:
    #     kMap.draw_region(tlx,tly,brx,bry,'blue')
    # kMap.mainloop()
    return ((tlx,tly),(brx,bry),legal)

# tests for 2 x 2
# print(is_legal_region([[0,0],[1,1]],[1,0]))
# print(is_legal_region([[1,1],[1,1]],[None,None]))
# print(is_legal_region([[0,1],[1,1]],[1,None]))
# print(is_legal_region([[0,1],[1,1]],[None,0]))


# tests for 2 x 4
# print(is_legal_region([[0,1,1,0],[1,1,'x',0]],[None,1,None]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0]],[None,None,None]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0]],[0,1,1]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0]],[None,0,0]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0]],[None,0,None]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0]],[1,1,None]))

# tests for 4 x 4
# print(is_legal_region([[0,1,1,0],[1,1,'x',0],[1,0,0,0],[0,0,0,0]],[1,0,0,1]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0],[1,0,0,0],[0,0,0,0]],[0,1,None,None]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0],[1,0,0,0],[0,0,0,0]],[None,None,1,0]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0],[1,0,0,0],[0,0,0,0]],[None,1,None,1]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0],[1,0,0,0],[0,0,0,0]],[None,1,None,0]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0],[1,0,0,0],[0,0,0,0]],[None,0,None,0]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0],[1,0,0,0],[0,0,0,0]],[None,0,None,1]))
# print(is_legal_region([[0,1,1,0],[1,1,'x',0],[1,0,0,0],[0,0,0,0]],[None,1,0,None]))
