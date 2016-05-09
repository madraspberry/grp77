import nltk
from nltk import IBMModel4, Alignment, AlignedSent

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
    
    src_classes = {
        'zero':0,
        'one':0,
        'two':0,
        'three':0,
        'four':0,
        'five':0,
        'six':0,
        'seven':0,
        'eight':0,
        'nine':0,
        'plus':1,
        'minus':1,
        'times':1,
        'divide':1}
    trg_classes ={
            '0':0,
            '1':0,
            '2':0,
            '3':0,
            '4':0,
            '5':0,
            '6':0,
            '7':0,
            '8':0,
            '9':0,
            '10':1,
            '11':1,
            '12':1,
            '13':1
        }
    ibm4 = IBMModel4(alignedSentences, 1, trg_classes, src_classes )
    
    percentages=[]
    percentages.append(format(ibm4.translation_table['one']['1']))
    percentages.append(format(ibm4.translation_table['two']['2']))
    percentages.append(format(ibm4.translation_table['three']['3']))
    percentages.append(format(ibm4.translation_table['four']['4']))
    percentages.append(format(ibm4.translation_table['five']['5']))
    percentages.append(format(ibm4.translation_table['six']['6']))
    percentages.append(format(ibm4.translation_table['seven']['7']))
    percentages.append(format(ibm4.translation_table['eight']['8']))
    percentages.append(format(ibm4.translation_table['nine']['9']))
    percentages.append(format(ibm4.translation_table['plus']['10']))
    percentages.append(format(ibm4.translation_table['minus']['11']))
    percentages.append(format(ibm4.translation_table['times']['12']))
    percentages.append(format(ibm4.translation_table['divide']['13']))
  
    sum = 0
    for number in percentages:
        sum += float(number)
    print(sum/13.0)	
    

    print("kex_2.py complete")

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
