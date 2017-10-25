from random import shuffle

def rearrange(words):
    words = list(words)
    shuffle(words)
    print (' '.join(words))

if __name__ == "__main__":
    import sys
    rearrange(sys.argv[1:])
