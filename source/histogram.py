import re
import time
'''
A histogram() function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
'''
'''
weighted frequecny taking the lfnght of a list of words then taking the word appears and divding it by the length'''

#data= open("histogram.txt", "r")
#source_text=data.read().replace('\n', '')
source_text="one fish two fish red fish blue fish"
#print(source_text)


def stringify(source_text):
    source_text=source_text.split(" ")
    source_text= ' '.join(source_text)
    source_text= source_text.split(",")
    source_text= ''.join(source_text)
    source_text= source_text.split(":")
    source_text= ''.join(source_text)
    source_text= source_text.split(";")
    source_text= ''.join(source_text)
    source_text= source_text.split(" \" ")
    source_text= ''.join(source_text)
    source_text= source_text.split(" ")
    return source_text

source_text= stringify(source_text)
print(source_text)

'''
There were quicker ways to do this but I specifically wanted the tokens and types as their own just incase that came up again in later programming
'''
def histogram(source_text):
    histogram = {}
    for word in source_text:
        if word not in histogram:
            histogram[word] = 0
        histogram[word] += 1


    print("As a dictionary: ",histogram)
    return (histogram)
#efficency testing
start = time.clock()
histo = histogram(source_text)
end = time.clock()
#print ("It took %.2gs  to run this" % (end-start))
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

    for key, value in histogram.items():
        if word in key:
            return(value)

test=frequency("blue",histo)

'''
takes the text from the source text and concerts it to a list of mini list that contain the word and its count
'''
def listogram(source_text):
    #empty list creation
    new_list = []
    #loops over each word in the source text
    for word in source_text:
        #if the word isnt in the new list....
        if word not in new_list:
            # in its own mini list, the word and its count are added
            new_list.append([word,source_text.count(word)])

    #used to get a new list without dupilcates
    listogram=[]
    for word in new_list:
        if word not in listogram:
            listogram.append(word)


    return listogram

listogram(source_text)
'''
Takes the source text and with it, creates a list of tuples with the count as well as word,
'''
def tuplegram(source_text):
    new_tuple=[]
    for word in source_text:
        if word not in new_tuple:
            new_tuple.append((word,source_text.count(word)))
    tuplegram=[]
    for word in new_tuple:
        if word not in tuplegram:
            tuplegram.append(word)
    return tuplegram

#print(tuplegram(source_text))
