import random
from random import shuffle
import itertools
def anagram(word):
    #turns the word into a list of characters
    s= list(str(word[0]))
    shuffle(s)
    print(''.join(s))
if __name__ == "__main__":
    # imports system for commandline
    import sys
    anagram(sys.argv[1:])
