import nltk
import copy
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
    tree_storage =[]

    """go through each line of input"""
    for line in content:
        """split each line into natural language and mrl"""
        s = line.split(':')
        natural = s[0].replace('"', '')
        natural = natural.split(" ")
        natural = list(filter(lambda a : a!= '', natural))

        mrl = s[1]
        mrl = list(filter(lambda a : a!= ' ', mrl))



        tree = parser.parse(mrl)
        temporary_tree_holder = parser.parse(mrl)
        for t in temporary_tree_holder:
            tree_storage.append(t)

        """Get all the rules used in the mrl"""
        edges = checker( tree, [])
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

    """This is the part where we SCFG"""


    """Create a dictionary"""
    mrlnat = {}
    mrlari ={
            '0':'0',
            '1':'1',
            '2':'2',
            '3':'3',
            '4':'4',
            '5':'5',
            '6':'6',
            '7':'7',
            '8':'8',
            '9':'9',
            '10':'+',
            '11':'-',
            '12':'/',
            '13':'*'
        }
    for x in meaning_matrix:
        
        if not input:
            print(x +"  " + repr(meaning_matrix[x].most_common(1)[0]) + "  " + repr(meaning_matrix[x]))
            mrlnat[meaning_matrix[x].most_common(1)[0][0]]= x
        if len(meaning_matrix[x]) == 1:
            ite = ite + 1

    """Need to get at the trees now """
    rules=[]
    for tree in tree_storage:
        extractor(tree, mrlnat,rules,mrlari)
    print("Recorded rules")
    rules = set(rules)
    for rule in rules:
        print(rule)	







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

"""Input is a tree"""
def extractor(input, mrlnat, rules, mrlari):

	if isinstance(input, nltk.tree.Tree):
		input.pretty_print()
		"""We are here meaning that the start node leads to at least one node."""
		if len(input) == 1:
			for node in input:
		
				res = extractor(node, mrlnat, rules, mrlari)
				
				if isinstance(node, nltk.tree.Tree):
					rules.append(input.label()+ " -> " + node.label())
					return repr(node.label())
					
				else:
					if res in mrlnat:
						rules.append(input.label() + " -> <" + mrlnat[res]  + ", " + mrlari[node]+ ">")
		else:
			temp =[]
			for node in input:
				if isinstance(node, nltk.tree.Tree):
					print("Located a tree of correct size" + input.label())
					temp.append(node.label())
					extractor(node, mrlnat, rules,mrlari)
				if len(temp) == 2:
					rules.append(input.label() + " -> <" + temp[0] +" " + mrlnat[input.label()] + " "  +temp[1] + ", (" +temp[0]+ mrlari[input.label()] +temp[1]+ ")>" )
	else:
		return input
		
if __name__ == "__main__":
     kex()

