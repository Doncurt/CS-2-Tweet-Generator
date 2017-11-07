'''
A histogram() function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
'''
'''
weighted frequecny takeking the lfnght of a list of words then taking the word appears and divding it by the length'''

source_text= "one fish two fish red fish blue fish".split(" ")
'''
There were quicker ways to do this but I specifically wanted the tokens and types as their own just incase that came up again in later programming
'''
def histogram(source_text):
    tokens = []
    types = []
    histogram=[]
    #get the tokens from the word list
    for i in range(len(source_text)):
        tokens.append(sum(x == source_text[i] for x in source_text))

    #get the types from the word list
    for word in source_text:
        types.append(word)

    #make the histogram as a list
    histogram = [[types[i], tokens[i]] for i in range(len(types))]

    # make into a tuple
    hist_tuple = set(tuple(element) for element in histogram)

    #make into a dictionary
    hist_dict = dict((types[i], tokens[i]) for i in range(len(histogram)))

    print("As a dictionary: ",hist_dict)
    return (hist_dict)

histo = histogram(source_text)

'''
A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.
'''
def unique_words(histogram):
    count = 0
    for key, value in histogram.items():
        if value == 1:
            count +=1
    print("The number of unique words is: ",count)
unique_words(histo)
'''
A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
'''
def frequency(word,histogram):
    word = str(sys.argv[1])
    for key, value in histogram.items():
        if word in key:
            return(value)
