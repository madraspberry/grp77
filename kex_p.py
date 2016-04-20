import nltk
from collections import Counter



def kex(input=None):
    """create grammar, read from file, create parser, create empty dictionaries"""
    grammar = nltk.data.load('file:arigram.cfg')

    if not input:
        with open("input-file-generated.txt") as f:
            content = f.read().splitlines()
    else:
        content = input

    parser = nltk.ChartParser(grammar)
    meaning_matrix = {}


    """go through each line of input"""
    for line in content:
        """split each line into natural language and mrl"""
        s = line.split(':')
        natural = s[0].replace('"', '')
        natural = natural.split(" ")
        natural = list(filter(lambda a : a!= '', natural))

        mrl = s[1]
        mrl = list(filter(lambda a : a!= ' ', mrl))



        t = parser.parse(mrl)

        """Get all the rules used in the mrl"""
        edges = checker( t, [])
        edges =list(filter(lambda a : a != 'S', edges))

        """Add occurences of nat to the dictionaries"""
        for word in natural:
            if len(meaning_matrix) == 0:
                meaning_matrix[word] = Counter(edges)

            elif word in meaning_matrix:
                for rule in list(meaning_matrix[word]):
                    if rule not in list(edges):
                        meaning_matrix[word] =  Counter(filter(lambda a : a!= rule, meaning_matrix[word]))
                    else:
                        meaning_matrix[word] += Counter([rule])

            else:
                meaning_matrix[word] = Counter(edges)

    ite = 0
    for x in meaning_matrix:

        if not input:
            print(x +"  " + repr(meaning_matrix[x].most_common(1)[0]) + "  " + repr(meaning_matrix[x]))
        if len(meaning_matrix[x]) == 1:
            ite = ite + 1

    procent = ite / len(meaning_matrix)
    """todo change procent printing to work with guesses"""
    if not input:
        print(str(procent*100) + "% guaranteed correct with current corpus of size " + str(len(content)))
        t = parser.parse(mrl)
        for it in t:
            it.pretty_print()

    return procent*100

"""def most_common(lst):
   return max(set(lst), key=lst.count)"""




def checker(input, ret ):
   for n in input:
    if isinstance(n, nltk.tree.Tree):
        if n.label() == 'S':
            checker(n, ret)
        if n.label() == '10':
            ret.append(n.label())
            checker(n, ret)
        if n.label() == '11':
            ret.append(n.label())
            checker(n, ret)
        if n.label() == '12':
            ret.append(n.label())
            checker(n, ret)
        if n.label() == '13':
            ret.append(n.label())
            checker(n, ret)
        else:
            ret.append(n.label())
   return ret


if __name__ == "__main__":
     kex()

