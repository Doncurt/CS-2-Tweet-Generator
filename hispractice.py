

'''
Histogram function that sorts the file first them starts the process of putting them into another file
'''
def histogram(hist):

    histofile = open("histogram.txt", "w+")
    for value, key in sorted(hist.items(), key=lambda s: s[1], reverse=True):
        histofile.write("%s, %s \n" % (value, key))
    histofile.close()


'''
takes the fine and accesses and sorts off of the  unique words that can be found in the file
'''
def unique_words(hist):

    unique_words = 0
    for word in input_histo:
        if hist[word] == 1:
            unique_words += 1
    return hist


# Prints whatever the word's frequency is
def frequency(hist, word):

    print_string = "The word '{}' shows up {} times."
    if word in input_histo:
        print(print_string.format(word, input_histo[word]))
    else:
        print("The word",  "'"+word+"'", "does not show up!")
    return hist.count(word)

if __name__ == '__main__':
    import sys
