from itertools import permutations

def CombineALL(string):
    words = string.split(',')
    cont = 0
    perm = permutations(words)

    with open("combination.csv", "a") as f:
        for i in list(perm):
            cont = cont + 1
            strc = str(i)
            strc = strc.replace(',', '')
            strc = strc.replace("'", "")
            strc = strc.replace(' ', '')
            strc = strc.replace('(', '')
            strc = strc.replace(')', '')
            print(strc)
            f.write(strc + "\n")

def WordToCombineNotAll(string):
    words = string.split(',')
    ct1 = len(words)

    a = 0
    first = ""
    while a < ct1:
        first = words[a]
        a = a + 1
        b = a
        while b < ct1:
            second = words[b]
            CombineALL(first + ',' + second)
            b = b + 1
            c = b
            while c < ct1:
                third = words[c]
                CombineALL(first + ',' + second + ',' + third)
                c = c + 1
                d = c
                while d < ct1:
                    fourth = words[d]
                    CombineALL(first + ',' + second + ',' + third + ',' + fourth)
                    d = d + 1
                    e = d
                    while e < ct1:
                        fifth = words[e]
                        CombineALL(first + ',' + second + ',' + third + ',' + fourth + ',' + fifth)
                        e = e + 1
                        f = e
                        while f < ct1:
                            sixth = words[f]
                            CombineALL(first + ',' + second + ',' + third + ',' + fourth + ',' + fifth + ',' + sixth)
                            f = f + 1

WordToCombineNotAll('!, info,@,info,September, 90')
