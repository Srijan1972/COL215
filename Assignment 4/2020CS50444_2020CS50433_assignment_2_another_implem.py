from K_map_gui_tk import *

getbinary = lambda x, n: format(x, 'b').zfill(n)

def xorcheck(x,y):
    p = 0
    for m in x:
        p = p | m
    q = 0
    for n in y:
        q = q | n
    r = p ^ q
    return r & (r-1) == 0

def get_term(term_list,vars):
    numvars = len(vars)
    term_str = ""
    term_list.sort()
    x = term_list[0] ^ term_list[-1]
    y = getbinary(x,numvars)
    z = getbinary(term_list[0],numvars)
    for i in range(numvars):
        if(y[i] == "0"):
            if(z[i] == "1"):
                term_str = term_str + vars[i]
            else:
                term_str = term_str + vars[i] + "\'"
    return term_str

def expandterm(term,true_bin,dc_bin,vars):
    print("current term expansion :",get_term(term,vars))
    x = term
    req = len(term)
    res = x
    for y in true_bin + dc_bin:
        if(x != y and xorcheck(x,y)):
            print("next legal terms :",get_term(y,vars))
            print("yems",x,y)
            res = x + y
            break
        elif(x != y):
            print("nos",x,y)
    print("expanded term :",get_term(res,vars))
    if(res == term or req == 2):
        return res
    else:
        return expandterm(res,true_bin,dc_bin,vars)

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
        true_bin.append([bin])
    for term in func_DC:
        bin = 0
        for var in vars:
            i = term.find(var)
            if i<len(term)-1 and term[i+1]=="'":
                bin = bin << 1 
            else:
                bin = (bin << 1) + 1
        dc_bin.append([bin])
    print(func_TRUE)
    print(true_bin)
    print(func_DC)
    print(dc_bin)
    for x in true_bin:
        ans.append(get_term(expandterm(x,true_bin,dc_bin,vars),vars))
    return ans
    

# func_TRUE = ["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'", "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"]
# func_DC = ["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]
func_TRUE = ["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"]
func_DC = ["abc'd"]
print(comb_function_expansion(func_TRUE,func_DC))
print("expected output:",["bc'","bc'","a'c'd","bc'","a'b'd"])
# L = [0,8]
# L2 = [4,12]
# print(get_term(L,["a","b","c","d"]))
# print(get_term(L2,["a","b","c","d"]))
# print(xorcheck(L,L2))