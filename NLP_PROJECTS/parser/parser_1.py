import nltk
import sys
nltk.download('punkt')


TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP
NP -> N | Det NP | AdjP NP | NP PP | NP Conj NP | Det AdjP NP 
VP -> V | V NP | V NP PP | V Adv | Adv V | Adv V NP
PP -> P NP | P NP PP
AdjP -> Adj | Adj AdjP | Adv AdjP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 3:
        with open(sys.argv[2]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print("np:",np)

def has_alphabet(string):
    for char in string:
        if char.isalpha():
            return True
    return False

def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    tokens = nltk.tokenize.word_tokenize(sentence)
    my_sentence = []
    for word in tokens:
        if not has_alphabet(word):
            tokens.remove(word)
        else:
            lowercase_word = word.lower()
            my_sentence.append(lowercase_word)
    return my_sentence

def look_for_NP(node,my_NPs_list):
    if isinstance(node, nltk.Tree):
        print(f"main_node:{node}")
        for child in node:  
            print(f"child:{child}")  
            if check_valid_NP(child):
                NP_list = traverse_tree(child,[])
                print(f"NP_LIST:{NP_list}")
                NP_phrase = " ".join(NP_list)
                my_NPs_list.append(NP_phrase)
            else:
                my_NPs_list = look_for_NP(child,my_NPs_list)
        return my_NPs_list 
    else:
        return my_NPs_list
            
def check_valid_NP(node):
    if isinstance(node, nltk.Tree):
        print(f"node.label():{node.label()}")
        if node.label() == "NP":
            for child in node:
                if check_valid_NP(child):
                    return False
            return True
        else:
            return False
    else:
        return False
def traverse_tree(node,NP_list):
    if isinstance(node, nltk.Tree):
        for child in node:
            NP_list = traverse_tree(child,NP_list)
        return NP_list
    else:
        NP_list.append(node)
        return NP_list

def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    return look_for_NP(tree,[])


if __name__ == "__main__":
    main()
