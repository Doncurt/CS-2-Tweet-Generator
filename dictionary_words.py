'''
A program that takes a command line number in put and spits out a number of random dictionary word(s)
all printingis done in the function so it acts as a black box
'''
#imports the random class to use
import random
#function declaration for dictionaryWords
def dictionaryWords(num):
    #turns the command line input into an in that can be used for processing
    num = int(num[0])
    # opens up the file and sets it to a list thats split by its lines
    lines = open('/usr/share/dict/words', 'rU').read().splitlines()
    #using the command entered value as a sentinel it determines the amount of times it must print
    for i in range (num):
        #takes a random index in the lines list and prints
        print (random.choice(lines))


#set up for command line arguments
if __name__ == '__main__':
#imports the system module
    import sys
    #sets up the
    dictionaryWords(sys.argv[1:])
