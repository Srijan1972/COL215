from K_map_gui_tk import *

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
    # print(N)
    # print(func_TRUE)
    # print(func_DC)
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
        ans_bin.append(used[i][0])
    for i in range(T):
        dc = 0
        for term,st in used:
            if i in st:
                x = 0
                for it in term:
                    if it == 'x':
                        x += 1
                if x > dc:
                    ans_bin[i] = term
                    dc = x
    # print(ans_bin[:K])
    ans = bin_to_min(ans_bin)
    return ans[:K]

# t1 = ["ab'cd'","abcd'"]
# d1 = ["a'b'cd"]
# print(comb_function_expansion(t1,d1))
# t2 = ["a'b'c'd", "a'b'c'd'", "a'b'cd'", "abcd'"]
# d2 = ["abc'd'", 'abcd', "a'bcd", "ab'cd'", "a'bc'd'", "a'b'c'd'"]
# print(comb_function_expansion(t2,d2))
# t3 = ["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"]
# d3 = ["abc'd"]
# print(comb_function_expansion(t3,d3))
# t4 = ["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'", "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"]
# d4 = ["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]
# print(comb_function_expansion(t4,d4))
# t5 = ["a'b'c'd'e'f'", "a'b'cd'ef", "a'b'cde'f", "a'bc'd'e'f'", "a'bc'd'ef", "a'bc'def", "a'bc'de'f", "ab'c'd'e'f", "ab'cd'e'f'"]
# d5 = ["abc'd'e'f", "abc'd'ef", "abc'def", "abc'de'f'"]
# print(comb_function_expansion(t5,d5))
# t6 = ["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'","a'b'cde", "a'bc'd'e'", "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'","ab'c'd'e","ab'c'de'","ab'c'de","ab'cd'e'","ab'cd'e","ab'cde'","ab'cde","abc'd'e'","abc'd'e","abc'de'","abc'de","abcd'e'","abcd'e","abcde'","abcde"]
# d6 = []
# print(comb_function_expansion(t6,d6))
# t7 = ["abc","a'bc","abc'","ab'c'"]
# d7 = ["ab'c"]
# print(comb_function_expansion(t7,d7))