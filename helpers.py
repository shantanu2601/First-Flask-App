from nltk.tokenize import sent_tokenize
def lines(a, b):
    """Return lines in both a and b"""
    list_a=[]
    list_b=[]
    list_c=[]
    line = ""
    for c in a:
        if c == '\n':
            if line not in list_a:
                list_a.append(line)
            continue
        else:
            line = line + c
    line = ""        
    for c in b:
        if c == '\n':
            if line not in list_b:
                list_b.append(line)
            continue
        else:
            line = line + c
    for c1 in list_a:
        for c2 in list_b:
            if c1 == c2:
                list_c.append(c1)
    return list_c


def sentences(a, b):
    """Return sentences in both a and b"""
    list_a = []
    list_b = []
    list_d = []
    list_a = sent_tokenize(a)
    list_b = sent_tokenize(b)
    for c1 in list_a:
        for c2 in list_b:
            if c1 == c2 and c1 not in list_d:
                list_d.append(c1)
    return list_d


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    list_c = []
    list_a = get_substrings(a,n)
    list_b = get_substrings(b,n)
    for c1 in list_a:
        for c2 in list_b:
            if c1 == c2 and c1 not in list_c:
                list_c.append(c1)
    return list_c

def get_substrings(a,n):
    output = []
    temp = len(a)-n+1
    for i in range(temp):
        output.append(a[i:n+i])
    return output   