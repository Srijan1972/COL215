def is_contained(T1,T2):
    assert(len(T1) == len(T2))
    n = len(T2)
    for i in range(n):
        if T2[i] == 'x':
            continue
        elif T2[i]!=T1[i]:
            return False
    return True

def can_take_common(T1,T2):
    assert(len(T1)==len(T2))
    diff_count = 0
    for i in range(len(T1)):
        if T1[i]!=T2[i]:
            diff_count += 1
    if diff_count == 1:
        i = 0
        while i < len(T1) and T1[i] == T2[i]:
            i += 1
        return i
    else:
        return -1

def bin_to_min(L):
    minterms = []
    for term in L:
        s = ""
        c = 97
        for ch in term:
            if ch == 0:
                s = s + chr(c) + "'"
            elif ch == 1:
                s = s + chr(c)
            c += 1
        minterms.append(s)
    return minterms

def remove_redun(redun,tMap):
    k = 0
    for i in range(len(redun)):
        rest_terms = []
        for j in range(len(redun)):
            if(k!=j):
                rest_terms+=tMap[redun[j]]
        if (all(x in rest_terms for x in tMap[redun[k]])):
            redun.remove(redun[k])
        else:
            k+=1
    return redun

def comb_function_expansion(func_TRUE, func_DC):
    """
    Determines the maximum legal region for each term in the K-map function
    Arguments:
        func_TRUE: list containing the terms for which the output is '1'
        func_DC: list containing the terms for which the output is 'x'
    Return:
        A list of terms: expanded terms in form of boolean literals
    """

    N = 0
    t = func_TRUE[0]
    K = len(func_TRUE)
    c = 97
    ans_bin = []
    vars = []
    while chr(c) in t:
        N+=1
        vars.append(chr(c))
        c+=1
    term_bin = []
    it = 0
    for term in func_TRUE:
        bin = []
        for var in vars:
            i = term.find(var)
            if i<len(term)-1 and term[i+1]=="'":
                bin.append(0)
            else:
                bin.append(1)
        term_bin.append((bin,{it}))
        it += 1
    for term in func_DC:
        bin = []
        for var in vars:
            i = term.find(var)
            if i<len(term)-1 and term[i+1]=="'":
                bin.append(0) 
            else:
                bin.append(1)
        term_bin.append((bin,{it}))
        it += 1
    T = len(term_bin)
    used = []
    while term_bin!=[]:
        M = len(term_bin)
        for i in range(M):
            for j in range(i+1,M):
                res = can_take_common(term_bin[i][0],term_bin[j][0])
                if res >= 0:
                    L = term_bin[i][0].copy()
                    L[res] = 'x'
                    terms = term_bin[i][1].union(term_bin[j][1])
                    term_bin.append((L,terms))
        for i in range(M):
            used.append(term_bin.pop(0))
    for i in range(T):
        ans_bin.append([used[i][0]])
    for i in range(T):
        dc = 0
        for term,st in used:
            if i in st:
                x = 0
                for it in term:
                    if it == 'x':
                        x += 1
                if x == dc:
                    ans_bin[i].append(term)
                if x > dc:
                    ans_bin[i] = [term]
                    dc = x
    temp = []
    for elem in ans_bin:
        for e in elem:
            temp.append(e)
    res = []
    [res.append(x) for x in temp if x not in res]
    return res

def opt_function_reduce(func_TRUE:list, func_DC):
    bin_poss = comb_function_expansion(func_TRUE,func_DC)
    ans = []
    N = 0
    t = func_TRUE[0]
    c = 97
    vars = []
    term_resol = {}
    while chr(c) in t:
        N+=1
        vars.append(chr(c))
        c+=1
    true_bin = []
    for term in func_TRUE:
        bin = []
        for var in vars:
            i = term.find(var)
            if i<len(term)-1 and term[i+1]=="'":
                bin.append(0)
            else:
                bin.append(1)
        true_bin.append(bin)
    n = len(bin_poss)
    for i in range(n):
        lt = []
        term = bin_poss[i]
        for elem in true_bin:
            if is_contained(elem,term):
                lt.append(elem)
        term_resol[bin_to_min([term])[0]] = lt
    # print(term_resol)
    # part 1
    while true_bin != []:
        n = len(bin_poss)
        L = [[] for i in range(n)]
        for i in range(n):
            term = bin_poss[i]
            for elem in true_bin:
                if is_contained(elem,term):
                    L[i].append(elem)
        mxsize = 0
        mxindex = -1
        mxterm = None
        for i in range(n):
            if len(L[i])>mxsize:
                mxsize = len(L[i])
                mxterm = bin_poss[i]
                mxindex = i
        if mxterm is not None:
            ans.append(mxterm)
            for elem in L[mxindex]:
                true_bin.remove(elem)
            bin_poss.remove(mxterm)
    ans = remove_redun(bin_to_min(ans),term_resol)
    return ans

