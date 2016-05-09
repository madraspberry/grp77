import nltk
from nltk import IBMModel1, Alignment, AlignedSent

def main():
    print("kex_2.py starting")

    grammar = nltk.data.load('file:arigram.cfg')
    parser = nltk.ChartParser(grammar)
    
    with open("input-file-generated.txt") as f:
        content = f.read().splitlines()

    alignedSentences = []
    for line in content:
        sentsRemovedQuote = line.replace('"','')
        alignedSents = sentsRemovedQuote.split(':')
        natural = alignedSents[0].split()
        mrl = alignedSents[1]
        mrl = list(filter(lambda a : a!= ' ', mrl))

        t = parser.parse(mrl)

        """Get all the rules used in the mrl"""
        edges = checker( t, [])
        edges =list(filter(lambda a : a != 'S', edges))
        
        alignedSentences.append(AlignedSent(natural, edges))
    
    ibm1 = IBMModel1(alignedSentences, 5)
	
    for result in alignedSentences:
        print(result.words)
        print(result.mots)
        print(result.alignment)


		
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

main()