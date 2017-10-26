#imports the random class
from random import shuffle

def madlibs(words):
    #turns the input into a list of wors
    words = list(words)
    #calls the shuffle class from random
    shuffle(words)
    #via .format() sets the entered text into formatting for output
    print ("there was once a {} who once ate a {}. And it tasted {}".format(words[0], words[1], words[2]))

if __name__ == "__main__":
    import sys
    print("plase enter only 3 words");

    madlibs(sys.argv[1:])
