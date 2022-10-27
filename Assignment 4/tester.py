from op import *

inputs =  [(["abc'd"], ["ab'c'd'", 'abcd', "ab'c'd", "ab'cd", "a'bcd'", "a'bc'd'", "a'b'cd", "a'b'cd'", "ab'cd'", "abcd'"]), (["a'b'c'd", "a'b'c'd'", "a'b'cd'", "abcd'"], ["abc'd'", 'abcd', "a'bcd", "ab'cd'", "a'bc'd'", "a'b'c'd'"]), (["ab'c'd", "abcd'", "a'bc'd"], ["a'b'cd", "ab'cd'", "a'bcd'", "abc'd'", "a'bcd"]), (["a'b'c'd", "a'b'cd'", "a'bc'd'", "a'bcd"], ["ab'c'd'", "abc'd'", "a'b'c'd'", "abc'd", "abcd'"]), (["ab'cd", "a'bcd'", "ab'c'd'", "abc'd", "a'b'cd'", "abc'd'"], ["ab'cd'", "a'b'cd", "a'b'c'd'", "a'bcd", "a'bc'd", "a'bc'd'", "a'b'c'd"]), (["a'b'cd", "a'b'c'd'", 'abcd', "ab'c'd'", "a'bcd"], ["a'bc'd", "a'b'c'd", "abc'd", "ab'c'd", "a'b'c'd'"]), (["a'b'cd", "abc'd'", "a'bcd'"], ["ab'c'd'", 'abcd', "a'bc'd", "ab'cd'", "abcd'"]), (["a'b'c'd'", "ab'c'd'", "a'bc'd'"], ["abc'd", "a'b'c'd'", "ab'cd", "abcd'", "a'b'cd'", "a'b'c'd"]), (["ab'cd", "a'b'cd'", "ab'cd'", "a'bcd"], ["ab'c'd", "a'bc'd'", "abc'd'", "abc'd", "a'bcd'", "abcd'", "a'b'c'd"]), (["abc'd", "a'b'c'd", "abcd'", "a'b'c'd'", "a'bc'd'"], ["ab'c'd'", "a'bc'd", "a'b'c'd'", 'abcd', "ab'c'd", "a'bcd'", "a'b'cd'", "abc'd'"]), (["ab'cd'e'", "a'bcd'e", "a'b'cde'", "a'bc'de", "a'b'cd'e", "abcd'e'", "ab'c'd'e'", "ab'cde'", "a'b'c'd'e", "a'b'c'de'", "ab'c'de'"], ["a'b'c'd'e'", "a'b'cde", "a'bcd'e'", "ab'c'd'e", "abcde'", "a'bc'd'e", "ab'cde", 'abcde', "abcd'e", "abc'de", "abc'd'e'"]), (["a'bc'd'e", "a'b'c'de'", "ab'c'd'e", "a'bcde", "ab'c'de", "abc'de'"], ["ab'cd'e", "ab'cde", "a'b'cd'e", "ab'c'de'", "abc'd'e", "a'bc'd'e'", "a'b'cde", "a'b'cd'e'", "a'b'cde'", "abcde'", 'abcde', "a'bc'de'"]), (["abc'd'e'", "a'b'cd'e", "a'bcde'", "a'b'c'd'e'", "ab'cde", "ab'cde'", "a'b'c'de'", "a'bc'd'e", "abcde'"], ["a'bcd'e'", "abc'd'e", "ab'c'de'", 'abcde', "a'bcd'e", "ab'c'd'e'", "a'bc'de'", "a'b'cd'e'", "a'b'c'd'e", "abcd'e'", "a'b'cde", "abcd'e", "a'b'cde'", "abc'de", "ab'cd'e'", "ab'cd'e"]), (["a'b'c'de'", "a'bcde'", "ab'c'de", "a'bc'de'", "abc'de"], ["abcd'e'", "abcd'e", "a'b'c'd'e'", "a'b'cd'e", "a'b'cd'e'", "ab'c'de'", "abc'de'", "abc'd'e'", "a'b'c'd'e", "a'b'c'd'e'", "a'bc'de", "ab'c'd'e'"]), (['abcde', "a'b'c'de", "a'bc'd'e'", "ab'cd'e", "abc'de'", "a'b'c'd'e", "ab'cd'e'", "ab'cde'", "a'b'cde"], ["ab'c'de", "abc'd'e'", "ab'c'de'", "a'b'c'de'", "a'b'cd'e", "a'bc'd'e", "abcd'e", "a'b'cde'"]), (["abcd'e", "ab'c'de'", "a'bcd'e'", "ab'cde", "a'b'cd'e'", "ab'c'd'e'", "a'bcd'e", "ab'c'de", "abc'de", "a'bc'de", "a'b'c'd'e'"], ["ab'cd'e", "a'b'cde", "abc'd'e'", "abc'd'e", "ab'cde'", "a'b'c'de'", "a'b'cd'e", "a'b'c'd'e'", "abc'de'", "a'bc'd'e", "a'b'cde'", "a'b'c'd'e", 'abcde', "a'bcde'"]), (["a'b'cde", "a'bcde'", "ab'c'd'e'", "ab'cd'e'", "a'b'cd'e", "ab'c'de", "abc'd'e'", "a'bc'd'e'", "a'b'c'd'e'", "a'bcde", "a'b'c'de'", "abc'd'e", "a'b'cd'e'", "ab'cde'"], ["a'b'c'd'e'", "ab'cde", "a'b'c'd'e", "a'bc'de", "abcde'", "a'bcd'e", "ab'cd'e", "ab'c'de'", "abc'de'", "a'bc'd'e", "abc'de", "abcd'e'"]), (["a'b'c'de", "abc'de'", "a'b'cd'e", "abc'de", "abcde'", "abcd'e", "ab'c'de", 'abcde'], ["ab'cd'e'", "a'bcd'e", "ab'c'de'", "a'b'cde'", "a'b'cde", "a'bc'd'e", "abcd'e'", "a'bc'de", "a'bcde", "ab'cd'e", "ab'cde'", "a'b'c'd'e'", "abc'd'e"]), (["a'b'c'd'e", "a'b'c'de'", "a'b'cd'e", "ab'cd'e", "a'bcde", "a'bc'de'", "abcd'e"], ["ab'c'd'e", "ab'c'd'e'", "abc'd'e", "a'b'cde'", "ab'cde'", "a'bcd'e'", "a'b'cd'e'", "ab'c'de", "abc'de'", "ab'c'de'", "a'bc'd'e'", "a'bcd'e", "abcd'e'", "a'b'cde", "abcde'", 'abcde', "a'b'c'd'e'", "a'b'c'de", "a'bc'd'e"]), (["a'b'c'de", "a'bcd'e", "abc'd'e", "a'b'c'de'", "a'bcde'", "a'bcd'e'", "ab'cd'e'", "abcd'e'", "ab'cde"], ["ab'cde'", "a'b'cd'e'", "a'b'cd'e", "a'b'c'd'e'", "ab'c'd'e", "ab'c'de'", "abc'de", "ab'cd'e", "a'bc'de'", "abc'de'", "a'bc'd'e", "a'bc'de", "abc'd'e'", 'abcde']), (["a'bc'def'", "abcde'f'", "a'b'c'de'f", "a'bc'd'e'f", "ab'cdef", "ab'cde'f'", "a'bcdef'", "a'b'cd'e'f", "abcd'e'f'", "a'b'cdef", "a'b'cde'f'", "a'bc'def", "abcdef'", "a'bcde'f", "abc'de'f", "ab'c'd'ef'", "a'bc'de'f"], ["ab'c'def'", "a'b'cd'ef", "ab'c'de'f'", "abc'de'f'", "a'b'c'def'", "abc'def", "abcd'ef'", "ab'c'd'e'f'", "ab'cd'ef", "a'bc'de'f'", "a'b'c'd'e'f'", "abc'def'", "a'bcde'f'", "abc'd'ef'", "a'bcd'e'f'", "a'b'cde'f", "a'b'cd'ef'", "ab'cd'e'f", "a'b'c'd'ef", "a'bcd'ef'", "a'bcd'e'f", "ab'c'def", "abc'd'e'f", "abcde'f", 'abcdef', "a'bcd'ef", "a'bc'd'e'f'", "ab'cde'f", "ab'c'de'f", "abcd'ef", "ab'c'd'e'f", "a'b'cd'e'f'", "a'b'c'd'e'f", "a'b'c'd'e'f'", "ab'cdef'"]), (["a'b'c'd'ef", "abc'd'ef'", "a'b'cd'e'f", "a'bcd'ef", "a'bc'd'e'f'", 'abcdef', "a'b'c'd'e'f", "a'b'c'def", "ab'c'def", "a'bcdef'", "ab'cd'e'f", "abc'def'", "abcd'ef", "a'bc'de'f", "a'b'c'd'e'f'", "abc'd'e'f'", "abcde'f'", "a'b'c'def'"], ["a'bc'def'", "a'bcd'ef'", "abc'd'e'f", "ab'cde'f", "abcd'ef'", "a'bc'de'f'", "abcde'f", "ab'cd'e'f'", "a'b'cd'ef'", "a'bc'd'e'f", "abc'd'ef", "a'bcd'e'f'", "ab'c'de'f", "a'b'c'de'f'", "a'bcdef", "abcd'e'f'", "a'bcde'f'", "ab'cde'f'", "a'bc'd'ef", "a'b'c'd'ef'", "abcd'e'f", "a'bc'd'ef'", "ab'cd'ef'", "abc'de'f'", "ab'c'd'e'f", "a'b'cdef", "a'b'cde'f", "a'b'c'de'f", "ab'cd'ef", "a'b'cd'ef", "ab'c'd'ef'", "ab'c'de'f'", "ab'c'd'e'f'", "a'b'cdef'"]), (["a'bcdef", "ab'cde'f", "abc'def", "a'b'c'd'e'f'", "a'bcd'e'f'", "a'bc'de'f", "ab'c'de'f'", "a'bc'd'ef'", "a'bcde'f", 'abcdef', "abcd'e'f", "a'b'cde'f'", "abcd'e'f'"], ["a'bc'd'ef", "a'b'c'd'e'f", "a'b'c'def'", "ab'cde'f'", "ab'c'de'f", "ab'cd'e'f", "abc'd'ef", "a'b'c'de'f", "a'bc'd'e'f'", "abcde'f", "ab'c'd'e'f'", "abc'def'", "a'bc'def'", "a'bc'de'f'", "a'b'cdef'", "abc'd'e'f", "ab'c'd'ef'", "ab'c'd'ef", "ab'cd'e'f'", "ab'cdef'", "a'b'c'de'f'", "abc'de'f'", "a'bcdef'", "a'bc'def", "a'b'cd'e'f", "abc'd'ef'", "a'b'cd'ef", "a'b'c'd'ef", "a'bcd'e'f"]), (["abc'def", "a'bc'd'e'f", "a'b'c'd'e'f'", "a'b'c'def", "abcd'ef'", "a'bc'd'ef", "a'b'cd'e'f", "ab'cd'ef", "a'b'cdef", "a'b'c'd'ef'"], ["abc'd'e'f", "a'b'c'de'f'", "abcd'ef", "a'bc'd'e'f'", "ab'c'd'ef", "a'b'c'd'ef", "abcde'f'", "a'b'cd'ef'", "ab'cde'f'", "a'bcd'e'f'", "a'b'cdef'", "a'b'c'de'f", "ab'cd'e'f'", "abc'de'f'", "a'bc'd'ef'", "abc'd'ef", "abcde'f", "a'bc'def", "a'bc'def'", "a'bcd'e'f", "ab'cd'e'f", "ab'c'd'e'f'", "abcd'e'f", "a'bcdef'", "a'bc'de'f'", "ab'cd'ef'", "a'b'cde'f", "ab'cde'f", "abc'd'e'f'", "ab'cdef'", "ab'c'def", "a'b'c'def'", "a'bc'de'f", "abcd'e'f'"]), (["ab'c'd'e'f'", "a'bc'def", "ab'c'd'e'f", "abc'd'e'f", "ab'cde'f", "a'b'cdef", "ab'cde'f'", "a'b'cd'ef'", "a'b'cde'f'", "abcde'f'", "ab'c'de'f'", "ab'cd'ef", "a'bc'd'ef'", "abc'd'ef'", "a'bcde'f'", "a'bc'de'f", "a'b'c'd'ef'", "a'b'c'de'f'", "abc'd'e'f'", "a'b'cd'e'f", "a'b'c'def'", "abcd'ef", "a'b'c'd'e'f'"], ["ab'c'def", "abcd'ef'", "a'bc'def'", "a'b'c'd'e'f", 'abcdef', "abc'd'ef", "a'b'c'd'ef", "ab'cd'ef'", "a'bc'd'ef", "a'b'c'd'e'f'", "a'bc'de'f'", "a'bcdef", "abcde'f", "abc'de'f", "ab'cdef'", "a'bc'd'e'f", "ab'cd'e'f", "a'b'cdef'", "abc'def", "a'bcd'ef", "abc'de'f'", "a'bcdef'", "a'b'cd'e'f'", "ab'c'd'ef", "ab'cdef", "a'b'c'de'f", "a'b'cde'f", "a'bcd'e'f"]), (["ab'cd'e'f", "abc'def", "a'bc'd'e'f", "ab'cde'f", "a'bc'de'f", "a'bcde'f", "ab'c'd'e'f", "ab'c'def", "a'bc'd'ef", "a'b'cd'ef'", "a'b'c'd'e'f"], ["abc'd'e'f'", "a'b'c'de'f", "abc'de'f'", "a'bcd'ef'", "a'b'cdef'", "a'b'c'd'ef", "abc'd'ef'", "a'b'cd'e'f", "abc'def'", 'abcdef', "ab'c'de'f'", "ab'cd'ef'", "a'b'cdef", "ab'cd'ef", "a'b'c'd'e'f'", "a'bc'd'ef'", "ab'cde'f'", "abcde'f'", "a'b'cde'f'", "a'b'c'd'e'f'", "a'b'cde'f", "ab'c'd'ef'", "ab'cdef'", "abcde'f", "abcd'e'f", "ab'c'd'e'f'"]), (["a'bcde'f", "a'bc'de'f", "ab'cd'ef'", "ab'c'd'e'f", "ab'cdef'", "a'b'cd'e'f'", "a'b'cde'f'", "a'bcd'e'f", "a'b'c'd'e'f'", "ab'c'd'ef", "ab'cd'ef", "abc'def'", "ab'c'de'f'", "a'bc'd'e'f'", "ab'c'de'f", "abcd'e'f"], ["a'b'cd'e'f", "abc'de'f'", "a'bcd'ef'", "abc'd'ef", "a'b'c'd'ef'", "a'bc'd'e'f", "abcd'e'f'", "a'b'c'def'", "a'b'cd'ef", "a'b'c'd'e'f'", "a'b'c'de'f", "a'b'cde'f", "abcdef'", "abc'd'ef'", "ab'c'def'", "a'bc'd'ef'", "abcde'f", "a'b'cdef'", "a'b'c'def", "a'b'c'de'f'", "abcde'f'", "ab'cde'f'", 'abcdef', "a'b'c'd'e'f", "ab'cde'f", "ab'c'def", "ab'cdef", "abc'd'e'f", "abc'def", "a'bcdef", "a'bc'def"]), (["a'bcde'f", "a'b'c'd'e'f'", "abc'd'ef'", "abc'def", "ab'cd'e'f", "a'b'cdef'", "ab'cdef'", "a'bc'd'e'f'", "abc'de'f", "a'bc'def'", "ab'c'd'ef'", "ab'c'd'e'f'", "a'b'c'd'e'f'", "ab'cd'ef", "ab'cd'ef'", "abc'def'", "a'b'c'def"], ["abc'd'e'f", "abcd'ef", "a'bcde'f'", "abc'd'ef", "ab'c'def", "ab'cd'e'f'", "abcde'f'", "a'b'c'de'f", "a'b'cd'ef", "a'bcd'e'f", "a'b'c'd'e'f", "a'b'cd'ef'", "abc'd'e'f'", "a'bcd'ef'", "ab'cde'f'", "ab'cdef", "abcd'ef'", "a'bc'd'e'f", "a'b'cde'f", "a'b'c'd'ef", "a'bc'd'ef'", "a'b'cdef", "abcd'e'f", "a'bcdef", "abcde'f", "abcd'e'f'", "abcdef'", "a'bc'd'ef", "a'bcd'e'f'", "a'b'c'de'f'"]), (["a'bc'de'f'", 'abcdef', "ab'cd'e'f", "abc'def", "abcd'e'f'", "a'bcd'e'f", "a'b'c'de'f", "a'bc'd'e'f", "abcd'ef", "a'bc'd'ef'", "a'b'cdef'", "a'b'cd'e'f'", "a'b'c'd'e'f", "ab'c'd'e'f"], ["abc'd'e'f", "a'bcd'e'f'", "a'bc'de'f", "a'b'c'def'", "a'bcd'ef", "a'bcdef", "ab'cd'e'f'", "a'bcde'f'", "a'b'cde'f", "abc'def'", "ab'c'de'f'", "ab'cd'ef", "ab'cdef", "ab'cde'f", "abc'd'ef'", "a'bcd'ef'", "a'b'c'd'ef'", "a'b'cd'ef", "abc'de'f'", "a'b'c'd'e'f'", "abcdef'", "abc'd'e'f'", "abc'de'f", "ab'cdef'", "a'b'cd'ef'", "a'bcdef'", "a'b'c'd'ef", "a'bc'd'ef", "abcd'e'f", "a'b'c'd'e'f'", "a'bcde'f", "abcde'f", "a'b'cdef", "a'b'c'de'f'", "ab'c'd'ef'", "ab'cde'f'", "a'b'c'def"]), (["a'b'c'd'e'f", 'abcdef', "abc'de'f", "a'bcd'ef", "a'b'c'd'e'f'", "ab'c'de'f", "abcd'e'f", "abc'de'f'", "ab'c'de'f'", "a'b'c'd'ef'", "ab'c'd'ef'", "ab'cdef", "a'b'c'd'ef", "ab'c'def", "a'bc'def"], ["ab'c'd'e'f", "a'bc'd'e'f", "a'b'cde'f'", "ab'c'd'e'f'", "a'b'cde'f", "a'b'cd'e'f", "a'bc'd'e'f'", "a'b'c'de'f'", "a'bcde'f'", "a'bcde'f", "a'bcd'e'f", "abcd'e'f'", "a'bc'de'f'", "ab'cde'f'", "abcd'ef", "ab'c'd'ef", "ab'cd'e'f", "a'b'cd'ef'", "a'bc'de'f", "a'b'c'd'e'f'", "a'bc'def'", "a'bcdef'", "abc'def", "ab'cd'e'f'", "a'b'c'def'", "a'bcdef", "a'b'c'def", "abcdef'", "a'b'cdef", "abcde'f", "ab'cdef'", "abc'd'ef", "abcde'f'"]), (["a'bc'de'fg'", "ab'cde'fg", "a'bcdefg", "a'bc'd'ef'g", "a'b'c'd'efg'", "a'bc'de'f'g'", "abcd'ef'g", "abc'd'e'fg", "abcdefg'", "a'b'c'd'e'fg'", "a'b'cd'e'fg", "a'bcd'ef'g", "abcd'e'fg'", "ab'c'de'fg'", "a'bcdef'g'", "abc'defg'", "a'b'c'd'ef'g'", "a'b'c'd'e'f'g'", "ab'c'd'ef'g'", "ab'c'defg", "ab'cde'fg'"], ["a'bcde'f'g'", "ab'c'd'e'f'g'", "a'bcde'fg", "abc'de'fg'", "a'bc'd'e'f'g'", "a'bc'de'fg", "ab'c'def'g'", "a'b'c'd'ef'g", "a'b'c'defg", "abc'd'e'f'g", "abc'd'e'fg'", "a'b'cd'efg'", "a'bcdefg'", "abc'd'ef'g", "ab'c'd'efg'", "ab'cde'f'g'", "ab'c'd'e'fg'", "a'b'c'def'g", "a'b'cd'e'f'g", "abcd'e'fg", "a'bc'd'e'fg'", "ab'cde'f'g", "ab'cdef'g", "a'b'c'd'e'f'g'", "abcde'fg'", "a'bcd'e'fg", "ab'cd'efg'", "ab'c'def'g", "a'bc'd'e'fg", "ab'c'de'fg", "ab'cd'ef'g'", "abc'd'efg'", "ab'c'd'e'fg", "abcde'f'g", "abcd'ef'g'", "a'bcd'e'f'g", "a'b'cde'fg'", "a'bc'defg", "a'bc'def'g'", "ab'cdef'g'", "abc'd'ef'g'", "a'b'cdef'g", "a'b'c'd'e'fg", "ab'c'd'ef'g", "a'bcd'e'fg'", "a'bc'def'g"]), (["a'bc'd'efg'", "a'bcde'fg'", "a'bc'de'f'g'", "abc'de'fg", "a'b'c'd'e'fg'", "a'b'c'd'e'fg", "a'bcde'f'g", "a'b'c'd'efg", "abc'd'efg'", "a'bc'de'fg", "a'b'cd'e'f'g", "ab'c'de'f'g'", "ab'cd'e'fg'", "a'b'cd'e'f'g'", "ab'cdefg", "a'b'cd'e'fg'", "ab'cd'e'f'g'", "a'bc'd'efg", "ab'cde'f'g'", "a'b'c'd'e'f'g'", "abcde'f'g", "a'bc'de'f'g", "a'bcdef'g", "ab'c'd'e'f'g", 'abcdefg', "a'b'c'd'ef'g", "a'bcd'e'f'g", "abcd'ef'g", "ab'cd'ef'g", "a'bc'd'e'f'g", "ab'c'd'ef'g"], ["abc'de'f'g'", "a'b'c'def'g", "a'b'c'de'f'g'", "a'bc'd'e'fg'", "a'b'cd'ef'g", "ab'c'defg", "a'bcd'e'f'g'", "a'b'c'defg", "a'bc'd'e'fg", "ab'c'd'efg'", "abcde'fg", "ab'cd'ef'g'", "a'b'cd'e'fg", "ab'c'd'e'fg'", "abc'd'efg", "abcd'e'fg'", "a'b'cdef'g'", "a'bc'defg", "ab'c'de'fg", "a'b'cde'f'g", "abc'def'g'", "ab'cde'fg", "a'b'cdefg", "abc'd'e'fg'", "a'b'c'd'efg'", "abc'd'ef'g'", "a'bcd'ef'g", "ab'c'def'g'", "a'b'c'defg'", "a'bc'd'ef'g", "a'bc'd'e'f'g'", "abcde'f'g'", "ab'c'd'ef'g'", "a'bcd'efg'", "a'bc'd'ef'g'", "a'b'cdef'g", "a'b'c'd'e'f'g", "ab'c'd'e'f'g'", "abcdef'g'", "a'b'cd'ef'g'", "abcd'e'f'g'", "abcde'fg'", "abc'def'g", "ab'c'def'g", "ab'cd'e'f'g", "abcd'efg", "ab'cdef'g", "a'bcdefg", "ab'cdefg'", "a'bcdefg'", "a'b'c'de'fg'", "a'bc'defg'", "a'b'c'd'e'f'g'", "a'bcdef'g'", "a'bc'de'fg'", "ab'c'de'f'g", "abcd'ef'g'", "a'bc'def'g'", "abcd'e'f'g", "ab'cd'e'fg", "abc'd'e'f'g", "ab'cd'efg'", "a'bcd'ef'g'", "a'b'cd'efg'", "abc'd'e'fg", "a'bcd'e'fg", "abc'de'fg'", "a'bcde'f'g'", "a'b'cd'efg", "a'b'c'd'ef'g'", "a'b'cde'f'g'", "a'bcd'e'fg'", "abcdefg'", "ab'cde'f'g", "ab'c'd'efg"]), (["a'b'c'd'e'f'g", "a'bc'd'e'f'g'", "ab'cd'e'f'g", "abcd'e'f'g", "a'bcd'e'f'g'", "ab'c'de'f'g'", "abc'd'ef'g'", "abc'd'e'f'g'", "abcd'ef'g", "a'bcd'e'f'g", "abc'de'fg'", "abcd'efg", "a'b'cd'efg'", "abc'd'efg'", "a'bc'de'fg'", "a'bcd'e'fg", "a'bcdef'g", "abc'de'f'g'", "a'bcd'e'fg'", "abcdef'g", "ab'cde'f'g'", "a'bc'd'ef'g'", "a'bcde'fg'", "a'bc'd'ef'g", "a'b'c'de'f'g", "a'b'cdef'g", "a'bc'def'g", "abcdefg'", "a'bc'de'f'g", "a'bcdefg'", "a'bcde'f'g"], ["a'bcd'ef'g", "a'b'c'd'e'f'g'", "abcdef'g'", "a'b'c'de'fg'", "a'bc'def'g'", "ab'c'd'efg'", "ab'cde'f'g", "ab'c'd'ef'g", "ab'c'de'f'g", "a'b'cde'f'g'", "a'bc'd'e'fg", "abc'def'g'", "a'b'cd'e'f'g", "abcd'e'f'g'", "a'b'c'def'g", "abc'd'e'fg", "abc'd'e'fg'", "a'bc'd'efg'", "a'b'c'de'f'g'", "a'bcd'efg'", "a'b'cde'f'g", "a'bc'd'e'f'g", "abc'defg'", "abc'd'ef'g", "ab'c'd'e'fg", "abcde'f'g'", "a'b'c'd'efg", "a'bcd'efg", "abcd'ef'g'", "a'b'cd'efg", "ab'c'de'fg'", "ab'cd'ef'g'", "ab'c'def'g'", "a'b'cdefg", "ab'cdefg'", "a'b'c'd'ef'g'", "ab'cd'e'fg'", "a'b'cd'e'fg", "ab'c'de'fg", "a'bc'd'efg", "abc'def'g", "a'b'cd'ef'g", "ab'cdef'g", "ab'c'd'e'fg'", "ab'c'd'e'f'g", "a'bc'de'f'g'", "a'b'cde'fg"]), (["ab'c'd'ef'g", "abc'de'fg", "a'b'cd'e'fg", "abcd'e'fg", "a'bcdef'g", "a'bc'd'ef'g'", "ab'cd'e'f'g", "abc'd'e'fg", "ab'c'def'g'", "abcd'e'fg'", "a'bcd'e'f'g", "abc'd'efg", "a'b'c'd'e'fg", "abc'de'f'g", "a'b'cdefg", "a'b'cde'f'g'", "abcde'fg'", "a'b'c'd'e'f'g'", "abc'd'efg'", "a'b'cde'fg'", "ab'c'def'g", "a'b'c'defg", "abc'd'e'f'g'"], ["abcd'efg", "ab'c'd'e'fg'", "ab'cde'f'g'", "ab'c'd'e'f'g", "abc'de'f'g'", "a'b'c'd'ef'g", "a'b'cd'efg'", "a'bcd'efg'", "ab'c'd'e'f'g'", "a'bc'd'e'f'g", "ab'cd'ef'g'", "abcd'e'f'g", "a'bcdef'g'", "ab'c'd'e'fg", "a'b'cd'ef'g", "a'bc'd'ef'g", "a'b'c'd'efg'", "ab'c'de'f'g", "abc'def'g'", "a'b'c'd'e'f'g", "a'b'cde'fg", "a'bcd'e'fg'", "abcde'f'g'", 'abcdefg', "a'bc'def'g'", "ab'cd'efg'", "a'b'c'd'efg", "ab'c'defg", "ab'cde'fg", "ab'cde'fg'", "abc'defg", "ab'cdef'g", "abc'd'e'fg'", "abc'd'ef'g'", "a'b'c'defg'", "ab'c'de'fg", "a'bc'de'fg", "ab'c'd'efg", "a'b'cd'efg", "a'bcdefg'", "abcd'efg'", "a'bcd'ef'g", "a'b'cdef'g", "a'b'cdef'g'", "a'bc'de'fg'", "abcd'e'f'g'", "a'b'cde'f'g"]), (["abc'd'e'f'g", "abc'd'e'fg'", "ab'cdefg'", "ab'c'd'ef'g", "a'bc'defg", "a'bcdefg", "a'bc'defg'", "a'bc'd'e'fg'", "a'b'c'd'e'fg", "a'bcd'ef'g'", "ab'c'd'efg", "a'b'c'd'e'f'g'", "ab'c'de'f'g'", "a'b'c'de'f'g", "ab'c'defg", "abc'd'e'f'g'", "ab'cd'efg'", 'abcdefg', "a'b'cde'f'g", "a'b'c'de'f'g'", "a'bc'def'g", "abc'd'ef'g'", "a'b'cd'e'f'g", "a'b'c'de'fg'", "a'b'c'defg'"], ["ab'c'd'e'f'g", "abcd'efg'", "abc'def'g'", "a'b'c'd'e'fg'", "abc'de'fg", "a'bcde'fg", "ab'cde'f'g'", "ab'cd'e'f'g'", "abcd'efg", "ab'c'd'e'f'g'", "ab'cd'e'fg'", "a'b'c'd'ef'g", "abcde'f'g", "ab'c'de'f'g", "a'b'cde'fg'", "abc'd'e'fg", "ab'cd'ef'g'", "abcdef'g", "abcd'e'f'g'", "a'bc'd'e'f'g", "a'b'cd'efg'", "abc'd'efg", "a'b'cd'ef'g'", "abcde'fg'", "ab'cd'efg", "ab'c'de'fg", "abcd'e'fg'", "abc'de'f'g", "abcdef'g'", "abc'defg", "a'bc'd'efg", "abc'defg'", "ab'c'def'g", "a'bc'de'fg", "a'bcde'fg'", "ab'c'de'fg'", "a'bc'de'f'g'", "a'b'cde'fg", "a'b'cdef'g", "ab'c'defg'", "ab'c'd'ef'g'", "a'bcde'f'g'", "a'b'cd'efg", "a'b'c'd'e'f'g"]), (["a'b'c'de'fg", "a'bc'd'e'fg", "a'bc'd'e'fg'", "a'b'cdef'g", "abc'defg'", "a'b'cde'fg'", "a'bc'd'e'f'g", "a'bcdefg", "a'b'cd'efg", "a'b'c'd'ef'g", "a'b'c'd'e'f'g'", "a'bc'defg", "ab'c'd'e'fg'", "a'b'c'de'fg'", "abcdefg'", "abc'd'efg'", "ab'cde'fg", "ab'cd'ef'g'", "ab'c'd'ef'g", "ab'c'd'e'fg", "abc'de'fg'", 'abcdefg', "a'b'c'd'e'f'g", "a'bcd'e'fg'"], ["a'bc'de'fg", "a'b'cd'ef'g'", "a'b'cd'e'fg", "a'b'cd'e'f'g'", "a'b'cde'f'g", "abcde'f'g", "abcd'e'fg'", "ab'cdefg", "abc'def'g'", "a'b'c'de'f'g'", "abc'd'e'f'g'", "ab'cd'e'fg'", "abc'd'ef'g'", "a'bcdef'g", "abc'd'efg", "ab'c'de'f'g'", "ab'c'd'e'f'g", "a'bcd'ef'g", "abcdef'g", "abcde'fg", "a'bc'd'e'f'g'", "ab'cde'f'g", "a'bcd'e'fg", "a'b'cde'f'g'", "ab'c'd'e'f'g'", "a'bcd'e'f'g'", "a'bcdefg'", "ab'c'd'efg'", "abc'de'fg", "ab'c'd'ef'g'", "ab'cd'ef'g", "a'bcde'fg'", "a'bc'def'g", "ab'cdefg'", "a'b'cd'e'fg'", "ab'c'de'f'g", "a'bc'de'f'g'", "a'bc'def'g'", "a'bcde'fg", "abcd'ef'g'", "abcd'e'fg", "ab'cde'f'g'"]), (["a'b'c'd'ef'g'", "ab'cdef'g", "abcde'fg'", "abc'd'ef'g'", "a'bc'defg", "ab'c'd'e'f'g'", "abcd'efg'", "a'b'c'd'e'f'g'", "a'b'c'de'f'g", "a'b'c'd'efg'", "ab'cde'fg", "a'b'cd'e'f'g", "a'b'cde'f'g'", "a'bcde'f'g", "a'bc'd'e'fg", "a'bcd'e'f'g", "a'b'c'def'g'", "ab'c'd'e'fg'", "ab'cdefg'", "ab'cd'ef'g'", "a'bc'defg'", "abc'd'e'f'g'", "a'b'cd'e'fg'", "a'bcdefg'"], ["abc'd'e'fg'", "a'b'c'd'e'fg", "a'bcd'e'f'g'", "abcdefg'", "a'bc'd'efg", "abc'def'g", "abcd'e'f'g", "a'bcd'efg'", "a'b'cd'e'f'g'", "a'bc'de'f'g'", "a'b'c'd'e'f'g'", "abc'd'ef'g", "abc'de'fg", "abc'def'g'", "ab'cd'e'f'g'", "ab'c'de'f'g'", "a'b'c'd'ef'g", "ab'c'd'ef'g", "abc'de'f'g'", "abc'de'fg'", "a'b'cd'ef'g", "abc'd'e'fg", "ab'cde'f'g", "abcde'f'g'", "abcde'f'g", "ab'c'defg'", "abcd'ef'g'", "a'bc'd'e'f'g'", "abcd'e'f'g'", "abcdef'g", "ab'cd'efg", "ab'cdef'g'", "ab'c'd'e'fg", "a'bc'd'e'f'g", "a'b'cd'e'fg", "abcd'efg", "a'bc'd'e'fg'", "ab'c'def'g", "a'b'cde'f'g", "a'b'cdef'g'", "abc'd'efg", "a'b'cd'efg", "ab'c'd'ef'g'", "abc'defg'", "a'bcd'ef'g'", "ab'cd'e'fg'", "ab'c'de'fg'"]), (["a'bc'd'e'f'g'", "ab'cd'efg", 'abcdefg', "ab'cd'e'f'g", "ab'cd'e'f'g'", "a'b'cdef'g", "ab'cd'ef'g", "a'bc'defg", "a'bcdef'g", "a'b'cde'fg", "a'b'c'defg'", "ab'c'de'f'g'", "a'b'cde'f'g", "abc'd'efg", "a'bc'def'g", "a'b'cd'ef'g", "abcd'ef'g", "a'bcde'f'g", "a'b'cd'e'f'g'", "ab'cdef'g'", "ab'cd'e'fg'", "a'bcd'e'fg", "ab'c'de'fg", "ab'cd'efg'", "a'b'c'd'e'f'g'", "a'b'c'd'ef'g'", "a'bcd'e'f'g", "a'bc'd'efg", "a'b'c'd'e'fg", "abcde'fg'", "ab'cdef'g", "abcdef'g", "ab'c'de'f'g", "abc'd'ef'g", "a'b'c'defg"], ["a'b'cde'f'g'", "abcd'e'f'g", "a'b'cd'efg'", "ab'c'd'ef'g", "abc'd'e'f'g'", "ab'cd'e'fg", "a'bcd'e'f'g'", "ab'c'def'g", "a'bc'de'f'g'", "ab'c'd'e'fg'", "abc'd'ef'g'", "abcdef'g'", "a'bc'd'ef'g'", "a'bc'd'efg'", "a'b'cdefg'", "abcd'e'fg", "ab'c'd'ef'g'", "a'bc'def'g'", "ab'cde'fg", "abcd'ef'g'", "a'b'cd'efg", "abc'def'g'", "a'bc'd'e'fg", "abcd'e'f'g'", "abcde'fg", "a'bc'defg'", "a'bcd'e'fg'", "a'b'cdef'g'", "a'b'c'def'g'", "abc'de'fg", "ab'cd'ef'g'", "a'bc'd'ef'g", "a'b'c'd'efg'", "ab'c'defg", "a'bcde'fg'", "abc'd'e'fg'", "ab'cdefg'", "a'bcd'ef'g", "a'b'c'de'fg'", "a'b'c'd'e'f'g", "a'b'c'd'e'fg'", "a'bc'd'e'f'g", "ab'c'd'efg", "abc'de'f'g", "abc'd'efg'", "abcd'efg", "abc'def'g", "a'bc'de'fg", "a'b'cd'e'fg", "a'b'c'd'e'f'g'", "a'bc'de'f'g", "a'b'cdefg", "a'bcdefg", "a'b'c'def'g", "a'b'c'de'f'g", "a'bcd'ef'g'", "ab'c'd'efg'", "abcd'e'fg'"]), (["abc'defg", "a'bc'de'fg", "a'bc'de'f'g'", "ab'c'de'f'g'", "abc'd'efg", "a'b'cdef'g'", "abcd'e'f'g", "ab'cd'e'fg", "abc'de'fg'", "a'b'cd'ef'g", "a'bcd'e'f'g", "abcde'f'g", "a'bc'de'f'g", "ab'c'd'efg", "a'b'cd'e'fg", "a'b'cde'f'g", "ab'c'd'e'fg'", "a'b'cd'e'fg'", "a'bcd'e'f'g'", "a'b'cd'efg'", "ab'cde'f'g'", "abc'd'efg'", "abc'defg'", "a'b'c'de'fg", "a'b'cde'fg", "abc'd'e'f'g", "a'bcd'e'fg'"], ["ab'cd'ef'g'", "a'b'cdefg", "a'b'cd'e'f'g'", "abcdefg'", "a'bcdefg'", "a'b'c'defg", "ab'c'd'efg'", "a'b'c'd'e'f'g", "ab'cd'efg'", "abcd'ef'g'", "a'b'cd'e'f'g", "ab'c'd'ef'g", "ab'c'def'g'", "a'bc'd'efg", "a'bc'def'g", "a'b'cd'ef'g'", "abcd'e'fg", "a'bc'd'e'fg", "a'bc'd'e'f'g", "ab'cdef'g'", "a'bcd'e'fg", "abc'd'e'f'g'", "ab'c'd'e'fg", "ab'c'd'e'f'g'", "a'b'c'de'f'g", "abcd'e'fg'", "a'bcde'f'g", "abc'd'ef'g", "a'bcd'efg'", "ab'cde'f'g", "a'b'cdefg'", "ab'c'def'g", "a'bc'de'fg'", "a'b'c'd'efg", "abc'd'e'fg", "a'bcdefg", "a'bcd'efg", "a'b'c'def'g'", "ab'c'de'fg'", "ab'cdefg", "a'b'c'd'e'f'g'", "ab'cd'ef'g", "ab'c'defg", "a'b'c'd'e'fg", "abc'de'f'g", "a'bc'd'efg'", "abcd'efg", "a'bc'def'g'", "a'bc'd'e'f'g'", "abc'd'e'fg'", "a'bcde'f'g'", "a'b'c'de'fg'", "ab'cd'e'f'g", "abc'de'fg", "ab'cde'fg", "a'b'c'de'f'g'", "abcd'ef'g", "a'bc'defg"]), (["a'bcd'e'fg", "ab'c'defg'", 'abcdefg', "abc'd'e'f'g", "ab'cdef'g'", "a'bcde'fg'", "a'bc'd'efg", "ab'c'def'g", "ab'cd'e'f'g", "ab'c'd'e'f'g", "ab'cdef'g", "a'b'c'defg", "ab'c'd'ef'g'", "ab'c'de'f'g'", "ab'cd'efg", "a'bcdef'g", "abc'd'e'f'g'", "abc'd'ef'g'", "a'b'cd'ef'g", "ab'cde'fg'", "a'bc'd'ef'g", "ab'cd'e'fg", "a'bc'def'g"], ["ab'c'de'fg", "ab'cd'ef'g'", "a'bc'defg'", "abc'de'fg'", "a'b'c'defg'", "a'b'cdef'g'", "abc'de'f'g'", "a'bc'd'e'f'g'", "abcd'e'f'g", "abc'd'efg'", "a'bcde'f'g", "a'b'cd'ef'g'", "a'bc'd'e'f'g", "a'b'c'de'fg", "a'bcd'efg", "ab'c'd'ef'g", "ab'cd'efg'", "a'b'cde'fg'", "abcdef'g", "ab'c'd'e'fg", "a'b'cde'fg", "a'bcd'e'f'g'", "ab'c'd'e'f'g'", "a'bc'de'fg", "abc'defg", "ab'c'def'g'", "a'b'c'd'e'f'g'", "ab'c'de'f'g", "a'bc'def'g'", "a'bcdefg", "a'b'cd'e'fg", "a'bcd'e'f'g", "abc'def'g", "a'bc'd'e'fg", "ab'cde'f'g", "a'b'cd'e'f'g'", "abcde'fg", "ab'c'defg", "a'bc'd'ef'g'", "abc'de'f'g", "abcd'efg'", "a'bcde'fg", "abc'def'g'"])]
outputs =  [[2], [3, 3, 3, 3], [4, 3, 3], [3, 3, 2, 4], [2, 1, 2, 2, 1, 2], [2, 2, 2, 2, 2], [4, 2, 3], [3, 3, 3], [3, 2, 2, 3], [1, 1, 2, 1, 1], [3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3], [4, 3, 3, 3, 3, 3], [3, 2, 2, 2, 2, 2, 2, 3, 2], [3, 4, 3, 3, 3], [4, 3, 4, 4, 4, 3, 4, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 4, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2], [3, 3, 3, 2, 3, 2, 3, 2], [2, 2, 2, 2, 3, 3, 2], [3, 3, 3, 3, 4, 3, 3, 3, 3], [3, 2, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 2, 3, 2, 4, 3], [3, 3, 3, 3, 3, 4, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 3, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4], [3, 3, 3, 3, 3, 3, 4, 3, 4, 3], [4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 4, 3, 3, 3, 3], [4, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4], [3, 3, 4, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 4, 3, 4], [3, 4, 3, 4, 3, 3, 3, 3, 4, 4, 3, 3, 4, 3, 3, 4, 4], [4, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, 3, 4], [3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3], [5, 5, 5, 5, 4, 5, 5, 4, 5, 4, 5, 5, 4, 5, 5, 5, 4, 4, 4, 5, 5], [3, 3, 3, 4, 3, 3, 3, 3, 4, 4, 3, 4, 3, 3, 4, 3, 3, 3, 3, 3, 3, 4, 3, 3, 5, 3, 3, 3, 3, 3, 3], [4, 4, 4, 5, 5, 4, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4, 5, 4, 4, 4, 4, 5, 4, 5, 4], [4, 4, 5, 4, 5, 5, 6, 4, 6, 4, 5, 4, 4, 5, 5, 5, 5, 5, 4, 5, 4, 5, 5], [5, 5, 6, 5, 5, 5, 5, 6, 5, 6, 5, 4, 4, 4, 5, 5, 5, 5, 5, 4, 6, 5, 5, 5, 5], [6, 5, 5, 6, 5, 5, 5, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5], [5, 5, 5, 4, 6, 4, 5, 4, 6, 6, 6, 5, 5, 5, 5, 5, 6, 4, 5, 4, 5, 4, 5, 5], [4, 4, 5, 4, 4, 4, 4, 4, 4, 5, 4, 6, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 5, 4, 5, 4, 4, 4, 5, 5, 4, 4, 4, 4, 4], [4, 4, 4, 5, 4, 5, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 4, 4, 4], [5, 5, 5, 4, 5, 5, 5, 4, 5, 4, 5, 5, 4, 4, 6, 5, 4, 4, 6, 6, 5, 5, 5]]
for test in range(len(inputs)):
    true, dc = inputs[test]
    output = comb_function_expansion(true, dc)
    output = list(map(lambda x: len(x) - x.count("'"), output))
    assert(output == outputs[test]),f"Test case {true} {dc} expected {outputs[test]} got {output}"
