def remove_redun(redun,tMap):
    k = 0
    for i in range(len(redun)):
        print(i,k)
        print(redun[k])
        rest_terms = []
        for j in range(len(redun)):
            if(k!=j):
                rest_terms+=tMap[redun[j]]
        # print(rest_terms)
        if (all(x in rest_terms for x in tMap[redun[k]])):
            redun.remove(redun[k])
        else:
            k+=1
    return redun

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
    # ans = ["" for i in range(len(func_TRUE)+len(func_DC))]
    ans_bin = []
    vars = []
    while chr(c) in t:
        N+=1
        vars.append(chr(c))
        c+=1
    term_bin = []
    it = 0
    print(N)
    print(func_TRUE)
    print(func_DC)
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
            # print(f"Current term: {bin_to_min([term_bin[i][0]])[0]}")
            for j in range(i+1,M):
                res = can_take_common(term_bin[i][0],term_bin[j][0])
                if res >= 0:
                    L = term_bin[i][0].copy()
                    L[res] = 'x'
                    terms = term_bin[i][1].union(term_bin[j][1])
                    # print(f"Terms {bin_to_min([term_bin[i][0]])[0]} and {bin_to_min([term_bin[j][0]])[0]} combined")
                    term_bin.append((L,terms))
                    # print(f"Term {bin_to_min([L])[0]} is generated")
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
        # else:
        #     temp.append(elem)
    # ans = bin_to_min(ans_bin)
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
    # getting map
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
    # part 2
    print(bin_to_min(ans))
    ans = remove_redun(bin_to_min(ans),term_resol)
    return ans

# t1 = ["ab'cd'","abcd'"]
# d1 = ["a'b'cd"]
# print(opt_function_reduce(t1,d1))
# t2 = ["a'b'c'd", "a'b'c'd'", "a'b'cd'", "abcd'"]
# d2 = ["abc'd'", 'abcd', "a'bcd", "ab'cd'", "a'bc'd'", "a'b'c'd'"]
# print(opt_function_reduce(t2,d2))
# t3 = ["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"]
# d3 = ["abc'd"]
# print(opt_function_reduce(t3,d3))
# t4 = ["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'", "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"]
# d4 = ["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]
# print(opt_function_reduce(t4,d4))
# t5 = ["a'b'c'd'e'f'", "a'b'cd'ef", "a'b'cde'f", "a'bc'd'e'f'", "a'bc'd'ef", "a'bc'def", "a'bc'de'f", "ab'c'd'e'f", "ab'cd'e'f'"]
# d5 = ["abc'd'e'f", "abc'd'ef", "abc'def", "abc'de'f'"]
# print(opt_function_reduce(t5,d5))
# t6 = ["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'","a'b'cde", "a'bc'd'e'", "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'","ab'c'd'e","ab'c'de'","ab'c'de","ab'cd'e'","ab'cd'e","ab'cde'","ab'cde","abc'd'e'","abc'd'e","abc'de'","abc'de","abcd'e'","abcd'e","abcde'","abcde"]
# d6 = []
# print(opt_function_reduce(t6,d6))
# t7 = ["abc","a'bc","abc'","ab'c'"]
# d7 = ["ab'c"]
# print(opt_function_reduce(t7,d7))
# t8 = ["abc'defg", "a'bc'de'fg", "a'bc'de'f'g'", "ab'c'de'f'g'", "abc'd'efg", "a'b'cdef'g'", "abcd'e'f'g", "ab'cd'e'fg", "abc'de'fg'", "a'b'cd'ef'g", "a'bcd'e'f'g", "abcde'f'g", "a'bc'de'f'g", "ab'c'd'efg", "a'b'cd'e'fg","ab'cde'f'g'", "abc'd'efg'", "abc'defg'", "abc'd'e'f'g", "a'bcd'e'fg'"]
# d8 = ["ab'cd'ef'g'", "a'b'cdefg", "a'b'cd'e'f'g'", "abcdefg'", "a'bcdefg'", "a'b'c'defg", "ab'c'd'efg'", "a'b'c'd'e'f'g", "ab'cd'efg'", "abcd'ef'g'", "a'b'cd'e'f'g", "ab'c'd'ef'g", "ab'c'def'g'", "a'bc'd'efg", "a'bc'def'g", "a'b'cd'ef'g'", "abcd'e'fg", "a'bc'd'e'fg", "a'bc'd'e'f'g", "ab'cdef'g'", "a'bcd'e'fg", "a'b'c'de'f'g", "abcd'e'fg'", "a'bcde'f'g", "abc'd'ef'g", "a'bcd'efg'", "ab'cde'f'g", "a'b'cdefg'", "ab'c'def'g", "a'bc'de'fg'", "a'b'c'd'efg", "abc'd'e'fg", "a'bcdefg", "a'bcd'efg", "a'b'c'def'g'", "ab'c'de'fg'","abc'd'e'fg'", "a'bcde'f'g'", "a'b'c'de'fg'", "ab'cd'e'f'g", "abc'de'fg", "ab'cde'fg", "a'b'c'de'f'g'", "abcd'ef'g", "a'bc'defg"]
# print(opt_function_reduce(t8,d8))
# t9 = ["abc'de'fghi'j", "a'bc'd'e'fghij'", "ab'c'd'e'fg'hi'j", "a'b'c'd'e'fghi'j'", "a'b'cd'e'f'g'h'i'j'", "a'bcde'f'g'hij'", "abcd'e'fg'hi'j", "abcdef'gh'ij'", "abcdef'ghi'j'", "ab'c'de'fghij'", "a'bcd'e'f'g'h'ij", "ab'cdefgh'i'j'", "a'b'cd'e'fgh'ij'", "ab'c'd'e'f'gh'ij", "a'bcde'fg'hij'", "ab'c'defg'h'i'j", "abc'def'g'h'i'j'", "abc'de'fg'h'ij", "abc'de'fg'hij'", "ab'c'd'e'f'g'hi'j", "a'b'cd'e'fg'h'i'j'", "ab'cde'f'gh'i'j'", "a'b'c'd'e'fg'hi'j'", "ab'cdef'ghi'j", "a'bc'd'ef'g'hi'j", "a'bcde'fghi'j'", "abcd'ef'g'h'i'j", "ab'c'd'e'fg'h'i'j'"]
# d9 = ["ab'c'd'e'fg'h'ij'", "abcdef'g'h'ij", "ab'c'def'ghi'j", "ab'cde'fghi'j", "a'bcd'efghij", "a'bc'd'e'fghi'j", "ab'c'd'e'f'g'h'i'j", "a'bc'd'ef'ghi'j'", "a'b'cde'f'gh'ij'", "a'b'cd'e'fg'hij", "ab'cd'ef'g'hi'j'", "a'b'cde'f'ghij'", "abc'defgh'i'j", "a'bcd'ef'g'h'ij'", "abcde'fg'h'i'j'", "a'bc'd'efg'hi'j", "ab'cd'ef'gh'ij'", "ab'cdefg'h'i'j'", "a'b'cd'efghij", "a'bc'd'efg'h'ij'", "ab'c'de'fg'h'i'j'", "abc'd'ef'gh'i'j'", "a'bc'd'e'f'gh'i'j", "a'b'cdef'gh'ij", "a'b'c'def'g'h'ij'", "a'bc'def'ghij", "a'b'cd'e'fg'h'i'j", "abc'd'efgh'i'j", "ab'c'def'g'hi'j'", "ab'cd'e'f'ghij'", "a'b'cde'fgh'ij", "ab'c'de'f'gh'i'j'", "ab'c'de'fghij", "ab'c'd'e'fg'hij'", "a'bc'def'g'h'i'j", "a'bcd'efghij'", "a'b'c'd'e'f'ghi'j", "a'b'cdefgh'i'j", "a'b'cd'e'f'g'hi'j'", "ab'c'defg'hi'j", "ab'cdefghi'j'", "abcde'fg'hij", "a'b'c'd'e'fghij", "ab'cd'e'fghij", "a'bc'def'gh'ij'", "ab'cde'fg'h'ij", "a'b'c'd'efg'hi'j", "abcdefg'hi'j", "abcde'fgh'i'j'"]
# print(opt_function_reduce(t9,d9))
# t10 = ["abc'de'fghi'j", "a'bc'd'e'fghij'", "ab'c'd'e'fg'hi'j", "a'b'c'd'e'fghi'j'", "a'b'cd'e'f'g'h'i'j'", "a'bcde'f'g'hij'", "abcd'e'fg'hi'j", "abcdef'gh'ij'", "a'bc'defgh'i'j'", "a'bc'defghij'", "a'b'cd'e'f'ghi'j", "a'bc'd'e'f'gh'ij'", "a'b'c'de'f'ghij", "a'bcdef'g'h'ij'", "ab'cde'fgh'ij", "ab'cd'ef'ghij'", "a'bcdefg'h'i'j", "ab'c'd'ef'gh'ij", "abc'def'gh'i'j'", "a'bcde'f'g'h'i'j'", "a'b'c'd'efg'hij'", "ab'cdefg'hij'", "a'b'c'd'ef'ghi'j'", "a'b'cd'e'f'ghij", "abc'defghi'j", "abcd'efghi'j'", "a'bc'de'f'g'hi'j'", "a'bc'def'g'hij'", "ab'c'd'efghij", "a'b'cd'ef'g'hi'j", "ab'cd'ef'ghi'j'", "a'bcdef'gh'ij'", "a'b'c'de'fghij", "abcd'e'fg'h'i'j'", "a'b'c'd'e'f'g'h'i'j'", "a'bc'd'e'f'gh'ij", "a'b'c'd'e'f'g'hij'", "a'b'cde'f'gh'i'j'", "a'bc'defg'hi'j", "a'b'cd'ef'g'hij'", "ab'cde'f'g'hij'", "a'b'c'd'ef'g'hij'", "a'b'c'de'fg'h'ij", "a'bc'def'ghi'j", "a'b'c'd'e'fg'h'ij'", "a'b'c'de'f'gh'i'j", "ab'c'd'ef'gh'i'j'", "a'b'cde'fghij'", "a'bc'd'efghij'", "a'b'cd'efg'h'ij'", "a'b'cd'ef'ghi'j", "a'bcde'f'g'hi'j'", "a'b'c'd'e'fg'h'i'j'", "a'bcd'e'fghi'j", "ab'c'd'e'f'ghi'j", "a'b'cde'fg'hij'", "abcdef'g'hij", "a'b'cd'e'f'g'hij", "a'b'c'de'fg'h'i'j'", "a'bcde'f'ghi'j'", "ab'c'def'g'hij", "a'bc'de'f'gh'i'j", "abc'def'gh'i'j", "a'bcde'fghij'", "abc'd'e'fg'h'i'j", "a'bc'd'e'f'g'hi'j'", "a'b'c'defg'h'i'j", "abc'de'f'gh'ij'", "a'b'c'def'g'h'i'j'", "abcde'f'g'hi'j'", "a'b'c'd'ef'gh'i'j", "ab'cd'e'fg'hij", "ab'cde'f'g'hi'j", "abcdef'ghi'j'", "ab'c'de'fghij'", "a'bcd'e'f'g'h'ij", "ab'cdefgh'i'j'", "a'b'cd'e'fgh'ij'", "ab'c'd'e'f'gh'ij", "a'bcde'fg'hij'", "ab'c'defg'h'i'j", "abc'def'g'h'i'j'", "abc'de'fg'h'ij", "abc'de'fg'hij'", "ab'c'd'e'f'g'hi'j", "a'b'cd'e'fg'h'i'j'", "ab'cde'f'gh'i'j'", "a'b'c'd'e'fg'hi'j'", "ab'cdef'ghi'j", "a'bc'd'ef'g'hi'j", "a'bcde'fghi'j'", "abcd'ef'g'h'i'j", "ab'c'd'e'fg'h'i'j'"]
# d10 = ["ab'c'd'e'fg'h'ij'", "abcdef'g'h'ij", "ab'c'def'ghi'j", "ab'cde'fghi'j", "a'bcd'efghij", "a'bc'd'e'fghi'j", "ab'c'd'e'f'g'h'i'j", "a'bc'd'ef'ghi'j'", "a'b'cde'f'gh'ij'", "a'b'cd'e'fg'hij", "ab'cd'ef'g'hi'j'", "a'b'cde'f'ghij'", "abc'defgh'i'j", "a'bcd'ef'g'h'ij'", "abcde'fg'h'i'j'", "a'bc'd'efg'hi'j", "ab'cd'ef'gh'ij'", "ab'cdefg'h'i'j'", "a'b'cd'efghij", "a'bc'd'efg'h'ij'", "ab'c'de'fg'h'i'j'", "abc'd'ef'gh'i'j'", "a'bc'd'e'f'gh'i'j", "a'b'cdef'gh'ij", "a'b'c'def'g'h'ij'", "a'bc'def'ghij", "a'b'cd'e'fg'h'i'j", "abc'd'efgh'i'j", "ab'c'def'g'hi'j'", "ab'cd'e'f'ghij'", "a'b'cde'fgh'ij", "ab'c'de'f'gh'i'j'", "ab'c'de'fghij", "ab'c'd'e'fg'hij'", "a'bc'def'g'h'i'j", "a'bcd'efghij'", "a'b'c'd'e'f'ghi'j", "a'b'cdefgh'i'j", "a'b'cd'e'f'g'hi'j'", "ab'c'defg'hi'j", "ab'cdefghi'j'", "abcde'fg'hij", "a'b'c'd'e'fghij", "ab'cd'e'fghij", "a'bc'def'gh'ij'", "ab'cde'fg'h'ij", "a'b'c'd'efg'hi'j", "abcdefg'hi'j", "abcde'fgh'i'j'", "ab'cd'e'f'g'h'ij'", "a'bc'd'e'fgh'i'j", "ab'cd'e'f'gh'i'j'", "a'b'c'de'f'ghij'", "a'bcdefghij", "abcd'e'f'g'hij", "a'bcde'f'ghij'", "a'bc'de'f'ghi'j'", "a'b'c'd'ef'g'h'ij'", "a'b'c'defg'hij", "a'b'c'd'ef'ghi'j", "a'b'c'defghij", "a'bcd'efgh'ij", "a'bc'd'ef'g'h'ij'", "ab'cd'ef'g'h'i'j", "abc'de'f'g'hi'j'", "abc'de'f'g'hij'", "a'b'cdefgh'ij", "a'bc'd'e'fgh'ij", "a'b'cd'ef'g'h'ij", "a'bc'de'fgh'i'j", "a'bc'de'fgh'i'j'", "a'b'cd'ef'g'h'i'j'", "a'b'cde'fg'hi'j'", "abcd'ef'gh'i'j'", "a'bc'd'efg'h'ij", "a'b'c'de'fg'h'ij'", "a'b'c'd'efg'hij", "a'bc'd'efg'hi'j'", "a'bcdef'g'h'ij", "abc'd'efghi'j'", "ab'c'defghi'j'", "ab'c'de'f'ghij'", "ab'c'd'ef'ghij", "a'b'c'de'f'g'hij'", "a'bcd'ef'gh'i'j'", "abc'd'e'fg'hij'", "a'bc'd'efgh'i'j", "a'b'c'def'gh'i'j'", "ab'c'de'f'g'h'i'j'", "a'bcdef'g'hij", "abcd'efg'hi'j'", "a'b'c'd'e'f'gh'ij", "a'b'c'd'e'f'g'h'i'j'", "a'bcde'fg'hi'j'", "ab'cdefghi'j", "ab'c'd'efgh'i'j'", "abc'd'efg'hi'j'", "a'bcdefg'h'ij'", "ab'cd'efg'hi'j'", "abc'd'e'fghi'j'", "abcd'efg'h'i'j", "abc'd'efg'h'i'j", "abcde'f'g'hij'", "a'bcde'fg'h'i'j", "abc'd'e'f'ghij", "a'b'cdef'ghij'", "a'b'cde'fg'h'ij", "a'b'cde'fgh'i'j'", "abc'de'fg'hi'j'", "a'b'c'd'efg'h'i'j'", 'abcdefghij', "ab'cde'fg'h'ij'", "a'bcd'e'fg'h'ij", "abc'de'f'g'h'ij'", "ab'c'd'efg'h'i'j", "a'b'cde'fghi'j'", "a'bc'd'e'f'g'h'ij'", "a'b'cde'f'ghi'j'", "a'bcd'ef'ghi'j'", "ab'c'def'g'h'i'j'", "a'b'c'defg'h'i'j'", "abcde'f'g'h'i'j", "a'bcd'efg'h'i'j", "a'b'cdef'gh'ij'", "abcd'e'fgh'ij", "abc'd'efg'h'ij'", "ab'cd'e'f'ghi'j", "abcd'efgh'ij", "a'b'c'de'f'ghi'j'", "a'bc'defg'h'i'j'", "a'bc'de'fg'h'i'j", "abcd'ef'g'h'ij'", "ab'cd'e'f'g'hi'j", "a'bc'd'ef'g'hij", "abc'def'ghij", "a'bcdef'g'hi'j", "a'bcd'efg'h'i'j'", "a'bc'def'g'h'ij'", "a'b'cd'efg'hi'j", "ab'c'de'fgh'i'j", "abc'de'fgh'ij", "a'bc'de'f'g'hij", "abcde'fgh'ij'", "a'b'cd'efg'hij", "a'b'c'd'ef'g'h'ij", "a'b'cde'f'g'h'ij", "a'bcd'e'fg'hi'j", "a'bcd'e'fg'hij", "ab'c'd'efgh'ij", "ab'cde'f'ghi'j'", "ab'c'de'f'gh'i'j", "a'b'cdef'gh'i'j", "a'b'cde'f'g'h'ij'", "ab'c'd'e'fg'hij", "ab'c'd'e'fghij'", "a'bc'd'e'f'g'h'i'j", "abcd'e'f'ghi'j'", "a'b'cde'f'g'hij", "abc'd'e'f'g'hij'", "a'b'cd'e'f'ghij'", "a'bcd'efg'h'ij", "a'bcd'ef'g'hi'j", "a'bcd'efgh'i'j'", "a'b'c'd'ef'g'hi'j'", "ab'cd'e'f'ghij", "a'bcd'e'fgh'ij'", "ab'cdef'ghij'", "ab'c'd'e'f'ghij'", "a'bc'd'ef'g'h'i'j", "ab'c'd'e'f'gh'i'j'", "abcd'e'fghij", "abcd'e'f'ghij", "a'b'c'd'e'f'ghij", "abcdef'g'h'i'j'", "a'bcd'ef'gh'i'j", "a'bc'd'e'f'g'hi'j", "abcde'f'g'hij", "a'b'cd'efghij'", "ab'cdefghij'", "abcd'efg'h'i'j'", "ab'cd'ef'g'h'ij", "ab'c'de'f'ghij", "abcd'e'f'g'hi'j'", "abcd'efghi'j", "abcd'ef'ghi'j'", "abcdef'ghij'", "a'bc'd'e'f'ghi'j", "a'b'c'd'e'f'g'h'i'j", "ab'c'def'gh'ij'", "ab'cdefg'hi'j", "abc'def'g'hi'j", "ab'c'd'ef'g'h'ij", "ab'c'defgh'i'j", "a'b'cde'f'g'h'i'j", "abcde'fghij", "ab'c'd'e'f'g'h'ij'", "a'b'cd'ef'g'h'ij'", "a'b'c'd'efghi'j"]
# print(opt_function_reduce(t10,d10))
# t11 = ["a'b'c'd'","a'b'cd"]
# d11 = ["a'bc'd'","abc'd'","ab'c'd'","a'b'c'd","a'bcd","abcd","ab'cd","a'b'cd'"]
# print(opt_function_reduce(t11,d11))
# t12 = ["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"]
# d12 = ["abc'd"]
# print(opt_function_reduce(t12,d12))
# t13 = ["a'b'c'd", "a'b'cd", "a'bc'd", "abc'd'","abc'd", "ab'c'd'", "ab'cd"]
# d13 = ["a'bc'd'", "a'bcd", "ab'c'd"]
# print(opt_function_reduce(t13,d13))
# t14 = ["a'b'c", "a'bc", "a'bc'", "ab'c'"]
# d14 = ["abc'"]
# print(opt_function_reduce(t14,d14))
# t15 = ["a'b'c'd'e'", "a'bc'd'e'", "abc'd'e'", "ab'c'd'e'", "abc'de'", "abcde'","a'bcde'", "a'bcd'e'", "abcd'e'", "a'bc'de", "abc'de", "abcde","a'bcde", "a'bcd'e", "abcd'e", "a'b'cd'e", "ab'cd'e"]
# d15 = []
# print(opt_function_reduce(t15,d15))

# counter example 1
t16 = ["abc'd","abcd","ab'c'd'","a'bcd'"]
d16 = ["abc'd'","ab'c'd","a'bcd","abcd'"]
print(opt_function_reduce(t16,d16))
