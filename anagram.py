#imports the shuffle module
from random import shuffle

def anagram(word):
    #turns the word into a list of characters the index is used becuase command line arguments are taken in a list format so the first word would be at index 0
    shuffled = list(str(word[0]))
    #shuffles words
    shuffle(shuffled)
    print(''.join(shuffled))
if __name__ == "__main__":
    # imports system for commandline
    import sys
    anagram(sys.argv[1:])
