#imports the shuffle from random
from random import shuffle

def rearrange(words):
    #due to how commandline handles the arguments, it must be converted to a list for proocessing
    words = list(words)
    #shuffle class is alled and the words are shuffled
    shuffle(words)
    #the list is randomized then rejoined as a single string
    print (' '.join(words))

if __name__ == "__main__":
    #preps system for output
    import sys
    #takes command line arguments
    rearrange(sys.argv[1:])
