from nltk.tokenize import sent_tokenize
def lines(a, b):
    """Return lines in both a and b"""
    lista=a.splitlines(0)
    listb=b.splitlines(0) 
    seta = set(lista) 
    setb = set(listb)
    x = seta & setb
    return x
    


def sentences(a, b):
    """Return sentences in both a and b"""
    lista=set(sent_tokenize(a))
    listb=set(sent_tokenize(b))
 
    return lista & listb



def substring_tokenize(str, n):
    substrings = []

    for i in range(len(str) - n + 1):
        substrings.append(str[i:i + n])

    return substrings


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    a_substrings = set(substring_tokenize(a, n))
    b_substrings = set(substring_tokenize(b, n))

    return a_substrings & b_substrings

##def substrings(a, b, n):
##    """Return substrings of length n in both a and b"""

##    lista=set([a[i:i+n] for i in range(0, len(a)-1)])
##    listb=set([b[j:j+n] for j in range(0, len(b)-1)])
    
 ##   return lista & listb
