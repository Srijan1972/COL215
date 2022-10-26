from sqlalchemy import true
from K_map_gui_tk import *

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
    c = 97
    ans = []
    vars = []
    while chr(c) in t:
        N+=1
        vars.append(chr(c))
        c+=1
    true_bin = []
    dc_bin = []
    for term in func_TRUE:
        bin = 0
        for var in vars:
            i = term.find(var)
            if i<len(term)-1 and term[i+1]=="'":
                bin = bin << 1
            else:
                bin = (bin << 1) + 1
        true_bin.append(bin)
    for term in func_DC:
        bin = 0
        for var in vars:
            i = term.find(var)
            if i<len(term)-1 and term[i+1]=="'":
                bin = bin << 1 
            else:
                bin = (bin << 1) + 1
        dc_bin.append(bin)
    print(true_bin)
    print(dc_bin)
    return ans
    

func_TRUE = ["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'", "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"]
func_DC = ["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]
func_TRUE = ["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"]
func_DC = ["abc'd"]
print(comb_function_expansion(func_TRUE,func_DC))